from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField


def query_register(query):
    def _wrapper(node):
        node_name = node.__name__.lower()[:-4]
        print node_name
        meta = query._meta
        meta.fields[node_name] = Node.Field(node)
        meta.fields['all_' + node_name] = DjangoFilterConnectionField(node)
        query._meta.fields[node_name] = Node.Field(node)
        setattr(query, '_meta', meta)
        return node

    return _wrapper


def node_register(node_list):
    def _wrapper(query):
        for node in node_list:
            node_name = node.__name__.lower()[:-4]
            meta = query._meta
            meta.fields[node_name] = Node.Field(node)
            meta.fields['all_'+node_name] = DjangoFilterConnectionField(node)
            setattr(query, '_meta', meta)
        return query

    return _wrapper
