from django.db import models

# Create your models here.

class Grid(models.Model):
    managerName = models.CharField(max_length = 20)
    managerNumber = models.CharField(max_length = 12)
    homeTeam = models.CharField(max_length = 20)
    visitingTeam = models.CharField(max_length = 20)
    dateOriginated = models.DateTimeField()
    gameDate = models.DateTimeField()
    gameType = models.CharField(max_length = 3)
    accessNumber = models.CharField(max_length = 12)
    active = models.CharField(max_length = 12, default = '10')
    name1 = models.CharField(max_length = 12, default = 1)
    name2 = models.CharField(max_length = 12, default = 2)
    name3 = models.CharField(max_length = 12, default = 3)
    name4 = models.CharField(max_length = 12, default = 4)
    name5 = models.CharField(max_length = 12, default = 5)
    name6 = models.CharField(max_length = 12, default = 6)
    name7 = models.CharField(max_length = 12, default = 7)
    name8 = models.CharField(max_length = 12, default = 8)
    name9 = models.CharField(max_length = 12, default = 9)
    name10 = models.CharField(max_length = 12, default = 10)
    name11 = models.CharField(max_length = 12, default = 11)
    name12 = models.CharField(max_length = 12, default = 12)
    name13 = models.CharField(max_length = 12, default = 13)
    name14 = models.CharField(max_length = 12, default = 14)
    name15 = models.CharField(max_length = 12, default = 15)
    name16 = models.CharField(max_length = 12, default = 16)
    name17 = models.CharField(max_length = 12, default = 17) 
    name18 = models.CharField(max_length = 12, default = 18) 
    name19 = models.CharField(max_length = 12, default = 19) 
    name20 = models.CharField(max_length = 12, default = 20) 
    name21 = models.CharField(max_length = 12, default = 21) 
    name22 = models.CharField(max_length = 12, default = 22)
    name23 = models.CharField(max_length = 12, default = 23)
    name24 = models.CharField(max_length = 12, default = 24)
    name25 = models.CharField(max_length = 12, default = 25)
    column1 = models.CharField(max_length = 12)
    column2 = models.CharField(max_length = 12)
    column3 = models.CharField(max_length = 12)
    column4 = models.CharField(max_length = 12)
    column5 = models.CharField(max_length = 12)
    column6 = models.CharField(max_length = 12)
    column7 = models.CharField(max_length = 12)
    column8 = models.CharField(max_length = 12)
    column9 = models.CharField(max_length = 12)
    column10 = models.CharField(max_length = 12)
    row1 = models.CharField(max_length = 12)
    row2 = models.CharField(max_length = 12)
    row3 = models.CharField(max_length = 12)
    row4 = models.CharField(max_length = 12)
    row5 = models.CharField(max_length = 12)
    row6 = models.CharField(max_length = 12)
    row7 = models.CharField(max_length = 12)
    row8 = models.CharField(max_length = 12)
    row9 = models.CharField(max_length = 12)
    row10 = models.CharField(max_length = 12)


    def __str__(self):
       a = self.id
       return str(a)





class Terms(models.Model):
    GRID = models.CharField(max_length = 100000, default = 1)
    MIN = models.CharField(max_length = 20)
    MAX = models.CharField(max_length = 20)
    PRICE =   models.CharField(max_length = 50)
    FIRST   =   models.CharField(max_length = 50)
    SECND =  models.CharField(max_length = 10)
    THIRD   =  models.CharField(max_length = 10)
    FINAL =  models.CharField(max_length = 20)
    FRTH =  models.CharField(max_length = 12)
    NOTES = models.CharField(max_length = 300)


    def __str__(self):
        b = self.id
        return str(b)

    

