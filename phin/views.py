from rest_framework import permissions
from dynamic_rest import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, list_route
from django_rdkit.models import *
import pandas as pd
from . import sql_helper
from . import models, serializers


class ActivitiesViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Activities.objects.all()
    serializer_class = serializers.ActivitiesSerializer

    @list_route(methods=['GET'], permission_classes=[permissions.AllowAny])
    def combined_activities(self, request):
        first_target_id = int(request.query_params['first_target'])
        second_target_id = int(request.query_params['second_target'])
        if (first_target_id > second_target_id):
            first_target_id, second_target_id = second_target_id, first_target_id
        top = int(request.query_params['top'])
        target_network = models.TargetNetwork.objects.get(
            first_target_id=first_target_id,
            second_target_id=second_target_id
        )
        mol_act = zip(target_network.molecule, target_network.mean)  # use mean value as default
        mol_act.sort(key=lambda x: x[1], reverse=True)
        if top > 0:  # return all if top is zero or negative.
            mol_act = mol_act[:top]
        molecule_id_list = map(lambda x: x[0], mol_act)
        result = models.Activities.objects.filter(
            Q(molecule_id__in=molecule_id_list),
            Q(target_id=first_target_id) | Q(target_id=second_target_id)
        ).order_by('molecule')
        if result:
            page = self.paginate_queryset(result)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(result, many=True)
            return Response(serializer.data)

        return Response(result)

    @list_route(methods=['GET'], permission_classes=[permissions.AllowAny])
    def molecule_combined_activities(self, request):
        first_molecule_id = int(request.query_params['first_molecule'])
        second_molecule_id = int(request.query_params['second_molecule'])
        if (first_molecule_id > second_molecule_id):
            first_molecule_id, second_molecule_id = second_molecule_id, first_molecule_id
        # top = int(request.query_params['top'])
        molecule_network = models.MoleculeInteraction.objects.get(
            first_molecule_id=first_molecule_id,
            second_molecule_id=second_molecule_id
        )
        # mol_act = zip(target_network.molecule, target_network.mean)  # use mean value as default
        # mol_act.sort(key=lambda x: x[1], reverse=True)
        # if top > 0:  # return all if top is zero or negative.
        #     mol_act = mol_act[:top]
        target_id_list = molecule_network.target
        result = models.Activities.objects.filter(
            Q(target_id__in=target_id_list),
            Q(molecule_id=first_molecule_id) | Q(molecule_id=second_molecule_id)
        ).order_by('target')
        if result:
            page = self.paginate_queryset(result)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(result, many=True)
            return Response(serializer.data)

        return Response(result)


class MoleculeViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Molecule.objects.all()
    serializer_class = serializers.MoleculeSerializer

    def get_queryset(self, *args, **kwargs):
        if 'search_type' in self.request.query_params:
            search_type = self.request.query_params.get('search_type')
            smiles = self.request.query_params.get('smiles')
            if search_type == 'substructure':
                return models.Molecule.objects.filter(structure__hassubstruct=QMOL(Value(smiles))).all()
            elif search_type == 'similarity':

                similarity = self.request.query_params.get('similarity')
                return models.Molecule.objects.structure_search(smiles, similarity)
        return models.Molecule.objects.all()


class ScaffoldActivitiesViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ScaffoldActivities.objects.all()
    serializer_class = serializers.ScaffoldActivitiesSerializer

    @list_route(methods=['GET'], permission_classes=[permissions.AllowAny])
    def combined_activities(self, request):
        first_target_id = int(request.query_params['first_target'])
        second_target_id = int(request.query_params['second_target'])
        top = int(request.query_params['top'])
        target_network = models.TargetScaffoldNetwork.objects.get(
            first_target_id=first_target_id,
            second_target_id=second_target_id
        )
        mol_act = zip(target_network.scaffold, target_network.mean)  # use mean value as default
        mol_act.sort(key=lambda x: x[1], reverse=True)
        if top > 0:  # return all if top is zero or negative.
            mol_act = mol_act[:top]
        scaffold_id_list = map(lambda x: x[0], mol_act)
        result = models.ScaffoldActivities.objects.filter(
            Q(scaffold_id__in=scaffold_id_list),
            Q(target_id=first_target_id) | Q(target_id=second_target_id)
        ).order_by('scaffold')
        if result:
            page = self.paginate_queryset(result)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(result, many=True)
            return Response(serializer.data)

        return Response(result)


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


class MoleculeInteractionViewSet(viewsets.DynamicModelViewSet):
    queryset = models.MoleculeInteraction.objects.all()
    serializer_class = serializers.MoleculeInteraction

    @list_route(methods=['GET'], permission_classes=[permissions.AllowAny])
    def molecule(self, request):
        mol = int(request.query_params.get('molregno'))
        parent_id = models.MoleculeHierarchy.objects.get(molregno=mol).parent.phin_molecule.mol_id
        result = models.MoleculeInteraction.objects.filter(
            Q(first_molecule_id=parent_id) | Q(second_molecule_id=parent_id)
        )
        if result:
            page = self.paginate_queryset(result)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(result, many=True)
            return Response(serializer.data)

        return Response(result)


class TargetNetworkViewSet(viewsets.DynamicModelViewSet):
    queryset = models.TargetNetwork.objects.all()
    serializer_class = serializers.TargetNetworkSerializer

    @list_route(methods=['GET'], permission_classes=[permissions.AllowAny])
    def target(self, request):
        tid = int(request.query_params.get('tid'))
        result = models.TargetNetwork.objects.filter(Q(first_target__tid=tid) | Q(second_target__tid=tid))
        if result:
            page = self.paginate_queryset(result)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(result, many=True)
            return Response(serializer.data)

        return Response(result)


class TargetScaffoldNetworkViewSet(viewsets.DynamicModelViewSet):
    queryset = models.TargetScaffoldNetwork.objects.all()
    serializer_class = serializers.TargetScaffoldNetworkSerializer

    @list_route(methods=['GET'], permission_classes=[permissions.AllowAny])
    def target(self, request):
        tid = int(request.query_params.get('tid'))
        result = models.TargetScaffoldNetwork.objects.filter(Q(first_target__tid=tid) | Q(second_target__tid=tid))
        if result:
            page = self.paginate_queryset(result)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(result, many=True)
            return Response(serializer.data)

        return Response(result)


# class TargetScaffoldInteractionViewSet(viewsets.DynamicModelViewSet):
#     queryset = models.TargetScaffoldInteraction.objects.all()
#     serializer_class = serializers.TargetScaffoldInteractionSerializer


class TargetViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Target.objects.all()
    serializer_class = serializers.TargetSerializer


class MMPViewSet(viewsets.DynamicModelViewSet):
    queryset = models.MMP.objects.all()
    serializer_class = serializers.MMPSerializer

    @list_route(methods=['GET'], permission_classes=[permissions.AllowAny])
    def molecule(self, request):
        molregno = int(request.query_params.get('molregno'))
        result = models.MMP.objects.filter(Q(RHMol_id=molregno) | Q(LHMol_id=molregno))
        if result:
            page = self.paginate_queryset(result)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(result, many=True)
            return Response(serializer.data)

        return Response(result)


class ICDViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ICD.objects.all().order_by('icd_id')
    serializer_class =serializers.ICDSerializer


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
