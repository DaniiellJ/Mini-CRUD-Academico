from django import forms
from .models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'curso', 'bio']
        widgets = {
            'nome': forms.TextInput(attrs={'maxlength': 100, 'required': True}),
            'curso': forms.TextInput(attrs={'maxlength': 100, 'required': True}),
            'bio': forms.Textarea(attrs={'placeholder': 'Digite uma breve biografia...'}),
        }
