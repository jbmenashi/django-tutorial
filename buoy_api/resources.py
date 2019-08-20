from tastypie.resources import ModelResource
from buoy_api.models import Symptom, Result


class SymptomResource(ModelResource):
    class Meta:
        queryset = Symptom.objects.all()
        resource_name = 'symptom'

class ResultResource(ModelResource):
    class Meta:
        queryset = Result.objects.all()
        resource_name = 'result'
