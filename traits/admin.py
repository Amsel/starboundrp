from django.contrib import admin

from character.admin import CharacterAdmin

from .models import Trait
# Register your models here.


@admin.register(Trait)
class TraitAdmin(admin.ModelAdmin):
    exclude = ('characters', 'trait_inline')
    inlines = []  # empty list, so the Trait inline is not inserted by default


class TraitInline(admin.StackedInline):
    model = Trait.characters.through
    extra = 1

CharacterAdmin.inlines.append(TraitInline)
