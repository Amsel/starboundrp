from django.shortcuts import get_list_or_404

from django.views.generic import ListView, DetailView

from character.models import Character

from traits.models import Trait


class CharacterList(ListView):
    model = Character


class CharacterDetail(DetailView):
    model = Character

    def get_context_data(self, **kwargs):
        # call base implementation
        context = super(CharacterDetail, self).get_context_data(**kwargs)

        context['trait_list'] = get_list_or_404(Trait)

        return context
