from django import template
from traits.models import Trait

register = template.Library()


@register.inclusion_tag('traits/character_trait_box.html')
def character_traits(character):
    traits = Trait.objects.filter(characters=character)
    return {'trait_list': traits}