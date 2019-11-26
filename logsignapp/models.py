from django.db import models
from django.contrib.auth.models import User

class Extenduser(models.Model):
    phone_num=models.CharField(max_length=100)
    age=models.IntegerField()
    user = models.OneToOneField(User,on_delete = models.CASCADE)

    
    


    
