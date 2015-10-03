from django import template
from django.shortcuts import get_list_or_404
from traits.models import Trait

register = template.Library()


@register.inclusion_tag('traits/character_trait_box.html')
def character_traits(character):
    traits = get_list_or_404(Trait)
    return {'trait_list': traits}