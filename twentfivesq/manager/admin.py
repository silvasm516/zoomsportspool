from django.contrib import admin

# Register your models here.
from django.contrib import admin
from manager.models import Managers
from manager.models import Purchases

class ManagersAdmin(admin.ModelAdmin):
    pass
admin.site.register(Managers, ManagersAdmin)


class PurchasesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Purchases, PurchasesAdmin)
