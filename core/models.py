from django.db import models


class Member(models.Model):
    member_name = models.CharField('Name', max_length=100)

    def __str__(self):
        return self.member_name


class Objective(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    objective_text = models.CharField('Objective', max_length=150)

    def __str__(self):
        return self.objective_text


class KeyResult(models.Model):
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE)
    kr_text = models.CharField('Key Result', max_length=200, blank=True)

    def __str__(self):
        return self.kr_text
