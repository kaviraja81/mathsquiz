from django.db import models

# Create your models here.
class Addition(models.Model):
    score=models.IntegerField()
 #   number1=models.ListField()
    category=models.CharField(max_length=2000)

