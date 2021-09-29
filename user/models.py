from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    phone = models.IntegerField()
    email = models.EmailField()
    age = models.IntegerField()
    username = models.CharField(max_length=100)
    

    def __str__(self):
        return '%s' %(self.username)