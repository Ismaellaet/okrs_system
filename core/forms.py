from django import forms

from .models import OKR


class OKRModelForm(forms.ModelForm):
    class Meta:
        model = OKR
        fields = '__all__'
