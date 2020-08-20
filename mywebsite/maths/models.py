from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Score(models.Model):
   username=models.ForeignKey(User,on_delete=models.CASCADE,related_name="score",null=True)
   score=models.IntegerField()
   grade=models.IntegerField(null=True)
 #   number1=models.ListField()
   category=models.CharField(max_length=2000)

