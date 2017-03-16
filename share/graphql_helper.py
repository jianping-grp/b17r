from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField


def _add_meta_prop(cls, dic):
    meta = cls._meta
    for k, v in dic.items():
        meta.fields[k] = v
        setattr(cls, '_meta', meta)


def query_register(query):
    def _wrapper(node):
        node_name = node.__name__.lower()[:-4]
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
            _add_meta_prop(
                query,
                {
                    node_name: Node.Field(node),
                    'all' + node_name: DjangoFilterConnectionField(node)
                }
            )
        return query

    return _wrapper
