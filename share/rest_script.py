from django.db.models.base import ModelBase

serializer_header = """
from . import models
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField


"""


def _list_models(app_model):
    for el in dir(app_model):
        cls = getattr(app_model, el)
        if type(cls) == ModelBase:
            yield cls


def _cls2serializer(cls):
    yield "class {0}Serializer:".format(cls.__name__)
    yield "    class Meta:"
    yield "        model = {0}".format(cls.__name__)
    yield "        exclude = []"


def create_serializers(app_model, file_path):
    with open(file_path, 'w') as w:
        w.write(serializer_header)
        for cls in _list_models(app_model):
            print cls.__name__
            for line in _cls2serializer(cls):
                w.write(line + '\n')
            w.write('\n')
