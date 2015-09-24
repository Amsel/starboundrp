from django.test import TestCase
from datetime import date
from .models import Character, Species


# Create your tests here.


class CharacterAgeTests(TestCase):
    def setUp(self):
        Species.objects.create(name="testdummy")

    def test_same_day_age(self):
        char = Character.objects.create(birth_date=date.today(), species=Species.objects.get(name='testdummy'))
        self.assertEqual(0, char.age())
