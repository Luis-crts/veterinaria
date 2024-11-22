from django import forms
from .modelos import Publicacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['nombre', 'descripcion', 'categoria', 'edad', 'imagen', 'ultima_pipeta', 'ultima_vacuna']
        widgets = {
            'ultima_pipeta': forms.DateInput(attrs={'type': 'date'}),
            'ultima_vacuna': forms.DateInput(attrs={'type': 'date'}),
        }
