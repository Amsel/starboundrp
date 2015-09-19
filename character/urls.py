from django.conf.urls import url

from .views import CharacterDetail, CharacterList

urlpatterns= [
    url(r'^$', CharacterList.as_view(), name='characters'),
    url(r'^(?P<pk>[0-9]+)/$', CharacterDetail.as_view(), name='character_detail'),
]
