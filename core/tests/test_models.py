from django.test import TestCase
from model_mommy import mommy

from core.models import Member, Objective, KeyResult


class MemberTestCase(TestCase):
    def setUp(self):
        self.member = mommy.make('Member')

    def test_str(self):
        self.assertEquals(str(self.member), self.member.member_name)


class ObjectiveTestCase(TestCase):
    def setUp(self):
        self.objective = mommy.make('Objective')

    def test_str(self):
        self.assertEquals(str(self.objective), self.objective.objective_text)


class KeyResultTestCase(TestCase):
    def setUp(self):
        self.key_result = mommy.make('KeyResult')

    def test_str(self):
        self.assertEquals(str(self.key_result), self.key_result.kr_text)
