from django.contrib import admin

# Register your models here.
from django.contrib import admin
from manager.models import Managers

class ManagersAdmin(admin.ModelAdmin):
    pass
admin.site.register(Managers, ManagersAdmin)
