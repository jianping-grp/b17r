import graphene
from graphene_django.debug import DjangoDebug
import chembl.schema


# todo: More Graphql resolver

class Query(chembl.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)
