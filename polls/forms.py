from django import forms
from .models import receita

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = receita
        fields = [
            'nome',
            'ingredientes',
            'tempo',
            'dificuldade',
            'instrucoes',
            ]