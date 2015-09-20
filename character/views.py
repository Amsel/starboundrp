from django.views.generic import ListView, DetailView

from character.models import Character


class CharacterList(ListView):
    model = Character


class CharacterDetail(DetailView):
    model = Character
