from django import forms
from .modelos import Publicacion

class PublicacionForm(forms.ModelForm):
    DURACIONES_PIPETA = [
        ('1', '1 mes'),
        ('3', '3 meses'),
        ('no', 'No ha sido suministrado')
    ]
    ESTADO_VACUNA = [
        ('1', '1 año'),
        ('no', 'No ha sido suministrado')
    ]
    
    duracion_pipeta = forms.ChoiceField(choices=DURACIONES_PIPETA, label="Duración de la pipeta")
    estado_vacuna = forms.ChoiceField(choices=ESTADO_VACUNA, label="Estado de la vacuna")
    
    class Meta:
        model = Publicacion
        fields = ['nombre', 'descripcion', 'categoria', 'edad', 'imagen', 'ultima_pipeta', 'ultima_vacuna']
        widgets = {
            'ultima_pipeta': forms.DateInput(attrs={'type': 'date'}),
            'ultima_vacuna': forms.DateInput(attrs={'type': 'date'}),
        }
