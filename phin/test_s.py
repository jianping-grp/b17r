from . import models
from . import serializers
target = models.Target.objects.all()[0]
target_inter = target.get_target_interaction().to_dict(orient='records')
ti = target_inter[0]