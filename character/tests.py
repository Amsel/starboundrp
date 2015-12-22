from django.test import TestCase
from datetime import date
from .models import Character, Species
from django.contrib.auth.models import User


# Create your tests here.


class CharacterAgeTests(TestCase):
    def setUp(self):
        Species.objects.create(name="testdummy")

    def test_same_day_age(self):
        char = Character.objects.create(birth_date=date.today(),
                                        species=Species.objects.get(name='testdummy'))
        self.assertEqual(0, char.age())


class AdminPanelTests(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('admin',
                                                       'admin@test.com',
                                                       'pass')

    def test_superuser_can_acces_user_propertys(self):
        self.client.login(username='admin', password='pass')
        response = self.client.get('/admin/auth/user/1/')
        self.assertEqual(response.status_code, 200)
