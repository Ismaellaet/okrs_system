from django.test import TestCase
from model_mommy import mommy


class MemberTestCase(TestCase):
    def setUp(self):
        self.member = mommy.make('Member')

    def test_str(self):
        self.assertEquals(str(self.member), self.member.name)


class OKRTestCase(TestCase):
    def setUp(self):
        self.okr = mommy.make('OKR')

    def test_str(self):
        self.assertEquals(str(self.okr), self.okr.objective)
