from django.db import models
from django.contrib.auth.models import User
from datetime import date
from dateutil.relativedelta import relativedelta

# Create your models here.


class Species(models.Model):
    name = models.CharField(max_length=127)


class Character(models.Model):
    first_name = models.CharField(max_length=127)
    # can be blank to support short names
    last_name = models.CharField(max_length=127, blank=True)
    birth_date = models.DateField()
    owner = models.OneToOneField(User, blank=True, null=True)

    species = models.ForeignKey(Species)
    # To embrace all kinds of special community members,
    # leave the User to input anything he wants here.
    gender = models.CharField(max_length=127, default='Unicorn')

    description = models.TextField(blank=True)
    biography = models.TextField(blank=True)
    picture_url = models.URLField(blank=True)
    color_code = models.CharField(max_length=127)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def age(self):
        return relativedelta(date.today(), self.birth_date)
