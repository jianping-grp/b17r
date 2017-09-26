from django.conf.urls import url
from rest_framework import routers
from . import views


routers = routers.DefaultRouter()
routers.register('activities', views.ActivitiesViewSet)
routers.register('molecules', views.MoleculeViewSet)
routers.register('scaffold-activities', views.ScaffoldActivitiesViewSet)
routers.register('scaffolds', views.ScaffoldViewSet)
routers.register('target-interactions', views.TargetInteractionViewSet)
routers.register('target-scaffold-interactions', views.TargetScaffoldInteractionViewSet)
routers.register('targets', views.TargetViewSet)

urlpatterns = routers.urls
urlpatterns += [
    url(r'^related-targets/(?P<target_id>[0-9]+)', views.get_related_target),
    url(r'^related-targets-list/', views.get_related_target_list)
]