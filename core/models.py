from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class OKR(models.Model):
    member = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    objective = models.CharField(max_length=150)
    key_result_1 = models.CharField(verbose_name='key result 1', max_length=200)
    key_result_2 = models.CharField(verbose_name='key result 2', max_length=200, blank=True, null=True)
    key_result_3 = models.CharField(verbose_name='key result 3', max_length=200, blank=True, null=True)
    key_result_4 = models.CharField(verbose_name='key result 4', max_length=200, blank=True, null=True)
    key_result_5 = models.CharField(verbose_name='key result 5', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.objective
