from django.db import models

# Create your models here.
class Suchi(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
class Basha(models.Model):
    name=models.ForeignKey(Suchi,on_delete=models.CASCADE)
    age=models.PositiveIntegerField()
    hobbies=models.CharField(max_length=100)
    
