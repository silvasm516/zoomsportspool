from django.contrib import admin

# Register your models here.
from django.contrib import admin
from player.models import Players

class PlayersAdmin(admin.ModelAdmin):
    pass
admin.site.register(Players, PlayersAdmin)
