from django.contrib import admin

from .models import *

from traits.admin import TraitInline

# Register your models here.


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    inlines = [TraitInline]


admin.site.register(Species)
