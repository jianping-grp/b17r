
from rest_framework import generics, permissions
from django.db import connection
from dynamic_rest import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
import pandas as pd
from . import sql_helper
from . import models, serializers


class ActivitiesViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Activities.objects.all()
    serializer_class = serializers.ActivitiesSerializer


class MoleculeViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Molecule.objects.all()
    serializer_class = serializers.MoleculeSerializer


class ScaffoldActivitiesViewSet(viewsets.DynamicModelViewSet):
    queryset = models.ScaffoldActivities.objects.all()
    serializer_class = serializers.ScaffoldActivitiesSerializer


class ScaffoldViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Scaffold.objects.all()
    serializer_class = serializers.ScaffoldSerializer


class TargetInteractionViewSet(viewsets.DynamicModelViewSet):
    queryset = models.TargetInteraction.objects.all()
    serializer_class = serializers.TargetInteractionSerializer


class TargetScaffoldInteractionViewSet(viewsets.DynamicModelViewSet):
    queryset = models.TargetScaffoldInteraction.objects.all()
    serializer_class = serializers.TargetScaffoldInteractionSerializer


class TargetViewSet(viewsets.DynamicModelViewSet):
    queryset = models.Target.objects.all()
    serializer_class = serializers.TargetSerializer


# custom api
@api_view(['GET'])
def get_related_target(request, tid):
    print tid
    target = models.Target.objects.get(tid=tid)
    related_targets = target.get_target_interaction().to_dict(orient='records')
    #print related_targets
    return Response(related_targets)


@api_view(['POST'])
def get_related_target_list(request):
    target_id_list = request.POST['target-id-list']
    print target_id_list
    with connection.cursor() as cursor:
        # use mean as default
        cursor.execute(sql_helper.TARGET_INTERACTION_LIST.format('mean', str(target_id_list)))
        data = pd.DataFrame(cursor.fetchall(), columns=['first_target', 'second_target', 'activity'])
        return Response(data.to_dict(orient='records'))

class TargetNetworkViewSet(viewsets.DynamicModelViewSet):
    
