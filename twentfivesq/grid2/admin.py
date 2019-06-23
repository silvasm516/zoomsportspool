from django.contrib import admin

# Register your models here.








from grid2.models import Grid
from django.db import models
from django.db.models import DEFERRED
class GridAdmin(admin.ModelAdmin):
    pass
    admin.site.register(Grid)
    fields = ('id', 'gameDate')
   
    




from grid2.models import Terms

class TermsAdmin(admin.ModelAdmin):
    pass
    admin.site.register(Terms)
