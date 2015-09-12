from django.views.generic import ListView

from character.models import Character


class CharacterList(ListView):
    model = Character

