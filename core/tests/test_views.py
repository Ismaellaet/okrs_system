from django.test import TestCase, Client
from django.urls import reverse

from model_mommy import mommy


class RegistrationTestCase(TestCase):
    def setUp(self):
        self.member = mommy.make('Member')
        self.data = {
            'member': self.member.id,
            'objective': 'Objective Test',
            'key_result_1': 'KR 1 Test',
            'key_result_2': 'KR 2 Test',
            'key_result_3': 'KR 3 Test',
            'key_result_4': 'KR 4 Test',
            'key_result_5': 'KR 5 Test'
        }
        self.client = Client()

    def test_register(self):
        response = self.client.post(reverse('core:register'), data=self.data)
        self.assertEquals(response.status_code, 201)

    def test_register_error(self):
        data = {
            'member': self.member.id,
            'objective_text': '',
            'kr_text': []
        }
        response = self.client.post(reverse('core:register'), data=data)
        self.assertEquals(response.status_code, 200)

    def test_index_view(self):
        response = self.client.get(reverse('core:index'))
        self.assertEquals(response.status_code, 200)
