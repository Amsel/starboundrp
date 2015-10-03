from django.shortcuts import get_list_or_404

from django.views.generic import ListView, DetailView

from character.models import Character

from traits.models import Trait


class CharacterList(ListView):
    model = Character


class CharacterDetail(DetailView):
    model = Character
