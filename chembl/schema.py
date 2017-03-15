from . import models as chembl_models
from graphene import AbstractType, Node
from graphene_django import DjangoObjectType
import django
from share.graphql_helper import query_register


class Query(AbstractType):
    pass


@query_register(Query)
class ActionTypeNode(DjangoObjectType):
    class Meta:
        model = chembl_models.ActionType
        interfaces = (Node,)


@query_register(Query)
class ActivitiesNode(DjangoObjectType):
    class Meta:
        model = chembl_models.Activities
        interfaces = (Node,)


@query_register(Query)
class ActivityStdsLookupNode(DjangoObjectType):
    class Meta:
        model = chembl_models.ActivityStdsLookup
        interfaces = (Node,)


@query_register(Query)
class AssayParametersNode(DjangoObjectType):
    class Meta:
        model = chembl_models.AssayParameters
        interfaces = (Node,)


@query_register(Query)
class AssayTypeNode(DjangoObjectType):
    class Meta:
        model = chembl_models.ActionType
        interfaces = (Node,)


@query_register(Query)
class AssaysNode(DjangoObjectType):
    class Meta:
        model = chembl_models.Assays
        interfaces = (Node,)

for attr in dir(chembl_models):
    if isinstance(chembl_models, django.db.models.ModelBase):
        pass # todo to be continue