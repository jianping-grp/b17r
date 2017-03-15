from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField


def query_register(query):
    def _wrapper(node):
        node_name = node.__name__.lower()[:-4]
        print node_name
        query._meta.fields[node_name] = Node.Field(node)
        setattr(query, 'all_' + node_name, DjangoFilterConnectionField(node))
        return node

    return _wrapper


def node_register(node_list):
    def _wrapper(query):
        for node in node_list:
            node_name = node.__name__.lower()[:-4]
            setattr(query, node_name, Node.Field(node))
            setattr(query, 'all_' + node_name, DjangoFilterConnectionField(node))
        return query

    return _wrapper
