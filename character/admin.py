from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    # this needs to be reset, since for some reason the traits inline gets also
    # applied to other admin sites
    # TODO research this! maybe some python magic
    inlines = []


admin.site.register(Species)
