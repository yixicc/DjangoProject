from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    age = models.IntegerField(default=3)
    data = models.IntegerField(null=True,blank=True)

class Department(models.Model):
    title = models.CharField(max_length=20)
