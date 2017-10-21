# import graphene
# from graphene_django.debug import DjangoDebug
# import chembl.schema
# import phin.schema
#
#
# class Query(chembl.schema.Query, phin.schema.Query, graphene.ObjectType):
#     debug = graphene.Field(DjangoDebug, name='__debug')
#
#
# schema = graphene.Schema(query=Query)
