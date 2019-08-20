from tastypie.resources import ModelResource
from buoy_api.models import Symptom, Result
from tastypie.authorization import Authorization


class SymptomResource(ModelResource):
    class Meta:
        queryset = Symptom.objects.all()
        resource_name = 'symptom'
        authorization = Authorization()

class ResultResource(ModelResource):
    class Meta:
        queryset = Result.objects.all()
        resource_name = 'result'
        authorization = Authorization()
