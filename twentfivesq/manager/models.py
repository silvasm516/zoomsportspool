from django.db import models

# Create your models here.
class Managers(models.Model):
    FirstName = models.CharField(max_length = 20)
    LastName = models.CharField(max_length = 20)
    Street =   models.CharField(max_length = 50)
    City   =   models.CharField(max_length = 50)
    ZipCode =  models.CharField(max_length = 10)
    State   =  models.CharField(max_length = 10)
    Country =  models.CharField(max_length = 20)
    UsrName =  models.CharField(max_length = 12)
    Password = models.CharField(max_length = 8, default=99990000)
    Email   =  models.EmailField(max_length = 20)  
    GridsPurch = models.IntegerField(default = 0)
    DollarPurch =   models.FloatField(max_length = 20, default = 0)
    GridsOut =   models.IntegerField(default = 0)



    def __str__(self):
        return self.LastName

class Purchases(models.Model):
    Date = models.DateField(auto_now=False, auto_now_add=False)
    UsrName = models.CharField(max_length = 20)
    GridsPch = models.IntegerField()
    Amount = models.FloatField(max_length = 20)

    def __int__(self):
        return self.id
