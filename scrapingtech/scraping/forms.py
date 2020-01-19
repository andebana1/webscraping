from django import forms
from .models import TechModel

class TechForms(forms.Form):
    title = forms.CharField(label="Buscar notícia", max_length=250)