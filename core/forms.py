from django import forms

from .models import Objective, KeyResult


class ObjectiveModelForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = ['member', 'objective_text']


class KeyResultModelForm(forms.ModelForm):
    class Meta:
        model = KeyResult
        fields = ['kr_text']
