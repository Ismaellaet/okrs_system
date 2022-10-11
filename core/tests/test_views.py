from django.test import TestCase, Client
from django.urls import reverse

from model_mommy import mommy


class RegistrationTestCase(TestCase):
    def setUp(self):
        self.member = mommy.make('Member')
        self.data = {
            'member': '1',
            'objective_text': 'My objective test',
            'kr_text': [
                'My key result 1',
                'My key result 2',
                'My key result 3',
                'My key result 4',
                'My key result 5',
            ]
        }
        self.client = Client()

    def test_registration(self):
        request = self.client.post(reverse('core:registration'), data=self.data)
        self.assertEquals(request.status_code, 200)

    def test_registration_error(self):
        data = {
            'member': '1',
            'objective_text': ' ',
            'kr_text': []
        }
        request = self.client.post(reverse('core:registration'), data=data)
        self.assertRaises(Exception)
