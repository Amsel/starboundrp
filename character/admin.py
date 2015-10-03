from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Species)
