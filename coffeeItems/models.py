from django.db import models
# Create your models here.
class Coffee(models.Model):
  name=models.CharField(max_length=250)
  price=models.FloatField()
  quantity=models.IntegerField()
  image=models.CharField(max_length=2083)

class Premium(models.Model):
  levels=models.CharField(max_length=50)
  cost=models.FloatField()
  value=models.CharField(max_length=30)
  
  

