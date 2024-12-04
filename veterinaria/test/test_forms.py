from django.test import TestCase
from veterinaria.forms import PublicacionForm

class PublicacionFormTest(TestCase):
    def test_form_valido(self):
        form_data = {'titulo': 'Prueba', 'contenido': 'Contenido'}
        form = PublicacionForm(data=form_data)
        self.assertTrue(form.is_valid())
