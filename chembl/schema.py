from . import models as chembl_models
from graphene import AbstractType, Node, resolve_only_args, ObjectType
from graphene_django import DjangoObjectType
from django.db.models import Model
from share.graphql_helper import node_register
import inspect
import graphene
from graphene_django.filter import DjangoFilterConnectionField

node_dic = {}
for cls_name, cls in inspect.getmembers(chembl_models, inspect.isclass):
    node = type(
        cls_name + 'Node',
        (DjangoObjectType,),
        {
            'Meta': type('Meta', (object,), {'model': cls, 'interfaces': (Node, )})
        }

    )
    node_dic[cls_name] = node

#node
@node_register(node_dic.values())
class Query(AbstractType):
    pass

class Activities(DjangoObjectType):
    class Meta:
        model = chembl_models.Activities
        interfaces = (Node, )


class Query2(AbstractType):
    bbb = Node.Field(Activities)
    aaa = DjangoFilterConnectionField(Activities)
