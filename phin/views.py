from rest_framework import generics, permissions
from django.db import connection
from dynamic_rest import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, detail_route, list_route
from rest_framework.viewsets import ViewSet
from rest_framework import generics
from django_rdkit.models import *
import pandas as pd
from . import sql_helper
from . import models, serializers


class ActivitiesViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Activities.objects.all()
    serializer_class = serializers.ActivitiesSerializer


class MoleculeViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Molecule.objects.all()
    serializer_class = serializers.MoleculeSerializer

    @list_route(methods=['POST', 'GET'], permission_classes=[permissions.AllowAny])
    def search(self, request):
        smiles = str(request.data['smiles'])
        similarity = float(request.data['similarity'])
        search_type = str(request.data['search type'])
        # perform substructure
        print smiles, similarity, search_type
        result = {}
        if search_type == 'substructure':
            result = models.Molecule.objects.filter(structure__hassubstruct=QMOL(Value(smiles))).all()
        # structure search
        else:
            try:
                result = models.Molecule.objects.structure_search(smiles, similarity)
            except:
                print 'structure search error'
        if result:
            page = self.paginate_queryset(result)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(result, many=True)
            return Response(serializer.data)

        return Response(result)


class ScaffoldActivitiesViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ScaffoldActivities.objects.all()
    serializer_class = serializers.ScaffoldActivitiesSerializer


class ScaffoldViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Scaffold.objects.all()
    serializer_class = serializers.ScaffoldSerializer

    @list_route(methods=['POST', 'GET'], permission_classes=[permissions.AllowAny])
    def search(self, request):
        smiles = str(request.data['smiles'])
        similarity = float(request.data['similarity'])
        search_type = str(request.data['search type'])
        # perform substructure
        print smiles, similarity, search_type
        result = {}
        if search_type == 'substructure':
            result = models.Scaffold.objects.filter(structure__hassubstruct=QMOL(Value(smiles))).all()
        # scaffold search
        else:
            try:
                result = models.Scaffold.objects.structure_search(smiles, similarity)
            except:
                print 'structure search error'
        if result:
            page = self.paginate_queryset(result)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(result, many=True)
            return Response(serializer.data)

        return Response(result)


class TargetInteractionViewSet(viewsets.DynamicModelViewSet):
    queryset = models.TargetInteraction.objects.all()
    serializer_class = serializers.TargetInteractionSerializer


class TargetScaffoldInteractionViewSet(viewsets.DynamicModelViewSet):
    queryset = models.TargetScaffoldInteraction.objects.all()
    serializer_class = serializers.TargetScaffoldInteractionSerializer


class TargetViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Target.objects.all()
    serializer_class = serializers.TargetSerializer


class MMPViewSet(viewsets.DynamicModelViewSet):
    queryset = models.MMP.objects.all()
    serializer_class = serializers.MMPSerializer


class KEGGDiseaseClassViewSet(viewsets.DynamicModelViewSet):
    # queryset = models.KEGGDiseaseClass.objects.all().annotate(
    #     targets_count=Count('get')
    # )
    queryset = models.KEGGDiseaseClass.objects.add_related_count(
        models.KEGGDiseaseClass.objects.all(),
        models.KEGGDisease,
        'kegg_class',
        'mapping_counts',
        cumulative=True
    )
    serializer_class = serializers.KEGGDiseaseClassSerializer


class KEGGDiseaseViewSet(viewsets.DynamicModelViewSet):
    queryset = models.KEGGDisease.objects.all()
    serializer_class = serializers.KEGGDiseaseSerializer


# custom api
@api_view(['GET'])
def get_related_target(request, target_id):
    target = models.Target.objects.get(target_id=target_id)
    related_targets = target.get_target_interaction().to_dict(orient='records')
    # print related_targets
    return Response(related_targets)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def get_related_target_list(request):
    target_id_list = request.POST['target-id-list']
    print target_id_list
    with connection.cursor() as cursor:
        # use mean as default
        cursor.execute(sql_helper.TARGET_INTERACTION_LIST.format('mean', str(target_id_list)))
        data = pd.DataFrame(cursor.fetchall(), columns=['first_target', 'second_target', 'activity'])
        return Response(data.to_dict(orient='records'))


class TargetScaffoldNetworkViewSet(generics.ListAPIView):
    queryset = models.TargetScaffoldInteraction.objects.all()

    # serializer_class = serializers.TargetNetworkSerializer

    def list(self, request, tid):
        # request.query_params.add('include[]', 'second_target.')
        target = models.Target.objects.get(tid_id=tid)
        queryset = models.TargetScaffoldInteraction.objects.get_target_interaction_agg(target.target_id)
        serializer = serializers.TargetScaffoldNetworkSerializer(
            queryset, many=True
        )
        return Response(serializer.data)


class TargetNetworkViewSet(generics.ListAPIView):
    queryset = models.TargetInteraction.objects.all()

    # serializer_class = serializers.TargetNetworkSerializer

    def list(self, request, tid):
        # request.query_params.add('include[]', 'second_target.')
        target = models.Target.objects.get(tid_id=tid)
        queryset = models.TargetInteraction.objects.get_target_interaction_agg(target.target_id)
        serializer = serializers.TargetNetworkSerializer(
            queryset, many=True
        )
        return Response(serializer.data)

# class TargetNetworkViewSet(viewsets.WithDynamicViewSetMixin, TargetNetworkViewSetRaw):
#     queryset = models.TargetInteraction.objects.all()
#     serializer_class = serializers.TargetNetworkSerializer
#     def list(self, request, target_id):
#         return super(TargetNetworkViewSetRaw, self).list(request, target_id)


# def retrieve(self, request, tid=None):
#     target = models.Target.objects.get(tid=tid)
#     related_targets = target.get_target_interaction().to_dict(orient='records')
#     serializer = serializers.TargetNetworkSerializer(related_targets, many=True)
#     return Response(serializer.data)
