from . import models as chembl_models
from graphene import AbstractType, Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django import DjangoObjectType

from share.graphql_helper import node_register


class ActionTypeNode(DjangoObjectType):
    class Meta:
        model = chembl_models.ActionType
        interfaces = (Node,)


class ActivitiesNode(DjangoObjectType):
    class Meta:
        model = chembl_models.Activities
        interfaces = (Node,)


@node_register([
    ActivitiesNode,
    ActionTypeNode
])
class Query(AbstractType):
    all_activities = Node.Field(ActivitiesNode)

