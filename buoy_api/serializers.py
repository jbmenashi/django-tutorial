from rest_framework import serializers
from .models import Symptom, Result


class SymptomSerializer(serializers.ModelSerializer):
   results = serializers.RelatedField(many=True)

   class Meta:
      model = Symptom
      fields = ['title', 'results']

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['title', 'frequency', 'symptom']


