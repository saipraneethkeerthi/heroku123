
from django.db import models

# Create your models here.

class projects(models.Model):
    name = models.CharField(max_length=100)
    dec = models.TextField()
    date= models.CharField(max_length=50)
    image= models.ImageField(upload_to='images')
    
class Myeducation(models.Model):
    year= models.CharField(max_length=20)
    study=models.CharField(max_length=100)
    college=models.CharField(max_length=500)
    branch=models.CharField(max_length=100)
    branchIs=models.BooleanField(default=False)
    cgpa=models.FloatField(max_length=10)