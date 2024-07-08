from django import forms
from .models import Candidato
from django.core.exceptions import ValidationError


class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nome', 'email', 'telefone', 'cargo', 'escolaridade', 'observacoes']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','id':'inputEmail3'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'escolaridade': forms.Select(attrs={'class': 'form-select','id':'autoSizingSelect'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_arquivo(self):
        arquivo = self.cleaned_data.get('arquivo')
        if arquivo:
            extensao = arquivo.name.split('.')[-1].lower()
            if extensao not in ['pdf','doc','docx']:
                raise ValidationError('Apenas arquivos PDF são permitidos.')
        return arquivo    