from django import forms
from .models import ElectronicsModel


class ElectronicForm(forms.ModelForm):
    class Meta:
        model = ElectronicsModel
        fields = ['name', 'content', 'slug', 'price', 'photo', 'category']
