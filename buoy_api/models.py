from django.db import models

class Symptom(models.Model):
   title = models.CharField(max_length=100)

   def __str__(self):
      return self.title

class Result(models.Model):
   title = models.CharField(max_length=100)
   frequency = models.IntegerField()
   symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)

   def __str__(self):
      return self.title
