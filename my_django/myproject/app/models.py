from django.db import models

# Create your models here.
class Oder(models.Model):
    id = models.IntegerField(auto_created=True, null=False, unique=True, primary_key=True)

class Customer(models.Model):
    userName = models.CharField(max_length=50, null=False, unique=True)
    passWord = models.CharField(max_length=100, null=False)
    createdDate = models.DateTimeField(auto_now_add= True)
    oder_id = models.ManyToManyField(Oder)