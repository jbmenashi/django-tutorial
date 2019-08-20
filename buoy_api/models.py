from django.db import models

# Create your models here.
class Symptom(models.Model):
   title = models.CharField(max_length=100)

class Result(models.Model):
   title = models.CharField(max_length=100)
   frequency = models.IntegerField()
   symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
