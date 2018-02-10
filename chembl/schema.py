from . import models as chembl_models
from graphene import AbstractType, Node, resolve_only_args, ObjectType
from graphene_django import DjangoObjectType
from django.db.models import Model
from share.graphql_helper import node_register
import inspect
import graphene
from graphene_django.filter import DjangoFilterConnectionField

# node_dic = {}
# for cls_name, cls in inspect.getmembers(chembl_models, inspect.isclass):
#     node = type(
#         cls_name + 'Node',
#         (DjangoObjectType,),
#         {
#             'Meta': type('Meta', (object,), {'model': cls, 'interfaces': (Node, )})
#         }
#
#     )
#     node_dic[cls_name] = node
#
# #node
# class ActivitiesNode(DjangoObjectType):
#     class Meta:
#         model = chembl_models.Activities
#         interfaces = (Node, )
#         filter_fields = {
#             'activity_comment': ['exact', 'icontains', 'istartswith']
#         }
#
# node_dic['Activities'] = ActivitiesNode
#
#
# @node_register(node_dic.values())
# class Query(AbstractType):
#     pass


###
class TargetDictionary(DjangoObjectType):
    class Meta:
        model = chembl_models.TargetDictionary
        filter_fields = ['pref_name', 'tid']
        interfaces = (Node,)



class Query(graphene.ObjectType):
    target_dictionary = Node.Field(TargetDictionary)
    all_target_dictionary = DjangoFilterConnectionField(TargetDictionary)
