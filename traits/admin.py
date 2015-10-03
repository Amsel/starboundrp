from django.contrib import admin

from .models import Trait

# Register your models here.


@admin.register(Trait)
class TraitAdmin(admin.ModelAdmin):
    exclude = ('characters',)


class TraitInline(admin.StackedInline):
    model = Trait.characters.through
    extra = 1

