import graphene
from graphene_django.debug import DjangoDebug
import chembl.schema


class Query(chembl.schema.Query, chembl.schema.Query2, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)
