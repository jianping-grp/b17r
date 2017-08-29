from django.db.models.base import ModelBase
from rest_framework.serializers import SerializerMetaclass
import inflect
import re

serializer_header = """
from . import models
from dynamic_rest import serializers


"""

viewset_header = """
from rest_framework import generics, permissions
from dynamic_rest import viewsets
from . import models, serializers


"""

url_header = """
from rest_framework import routers
from . import views


routers = routers.DefaultRouter()
"""


def _list_classes(app_model, cls):
    for el in dir(app_model):
        obj = getattr(app_model, el)
        if type(obj) == cls:
            yield obj


def _cls2serializer(cls):
    yield "class {0}Serializer(serializers.DynamicModelSerializer):".format(cls.__name__)
    yield "    class Meta:"
    yield "        model = models.{0}".format(cls.__name__)
    yield "        exclude = []"


def _serializers2viewsets(cls):
    cls_name = cls.__name__[:-10]
    yield "class {0}ViewSet(viewsets.DynamicModelViewSet):".format(cls_name)
    yield "    queryset = models.{0}.objects.all()".format(cls_name)
    yield "    serializer_class = serializers.{0}".format(cls.__name__)


def _url_name(cls_name):
    p = inflect.engine()
    word_list = re.findall('[A-Z][^A-Z]*', cls_name)
    word_list = [x.lower() for x in word_list]
    if not word_list[-1].endswith('s'):
        word_list[-1] = p.plural(word_list[-1])
    return '-'.join(word_list)


def _viewsets2url(cls):
    cls_name = cls.__name__[:-7]
    url_name = _url_name(cls_name)
    yield "routers.register('{0}', views.{1})".format(url_name, cls.__name__)


def create_serializers(app_model, file_path):
    with open(file_path, 'w') as w:
        w.write(serializer_header)
        for cls in _list_classes(app_model, ModelBase):
            print cls.__name__
            for line in _cls2serializer(cls):
                w.write(line + '\n')
            w.write('\n' + '\n')


def create_viewsets(app_serializers, file_path):
    with open(file_path, 'w') as w:
        w.write(viewset_header)
        for cls in _list_classes(app_serializers, SerializerMetaclass):
            print cls.__name__
            for line in _serializers2viewsets(cls):
                w.write(line + '\n')
            w.write('\n' + '\n')


def create_urls(app_views, file_path):
    with open(file_path, 'w') as w:
        w.write(url_header)
        for cls in _list_classes(app_views, type):
            print cls.__name__
            for line in _viewsets2url(cls):
                w.write(line + '\n')


def run():
    from phin import models
    create_serializers(models, 'phin/serializers.py')
    from phin import serializers
    create_viewsets(serializers, 'phin/views.py')
    from phin import views
    create_urls(views, 'phin/urls.py')
