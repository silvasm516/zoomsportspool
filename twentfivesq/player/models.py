from django.db import models

# Create your models here.
class Players(models.Model):
    FirstName = models.CharField(max_length = 20)
    LastName = models.CharField(max_length = 20)
    Street =   models.CharField(max_length = 50)
    City   =   models.CharField(max_length = 50)
    ZipCode =  models.CharField(max_length = 10)
    State   =  models.CharField(max_length = 10)
    Country =  models.CharField(max_length = 20)
    UsrName =  models.CharField(max_length = 12)
    Email   =  models.EmailField(max_length = 20)  





    def __str__(self):
        return self.LastName
