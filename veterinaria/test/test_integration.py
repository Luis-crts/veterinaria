from django.test import TestCase
from django.urls import reverse
from veterinaria.modelos import Publicacion
from veterinaria.forms import PublicacionForm

class IntegracionTest(TestCase):
    def test_formulario_y_vista(self):
        form_data = {
            'titulo': 'Prueba de Integración',
            'contenido': 'Este es un contenido de prueba.',
            'estado_vacuna': 'completado'
        }
        
        form = PublicacionForm(data=form_data)
        self.assertTrue(form.is_valid())
        
        publicacion = form.save()
        self.assertIsInstance(publicacion, Publicacion)
        
        self.assertEqual(publicacion.titulo, 'Prueba de Integración')
        self.assertEqual(publicacion.contenido, 'Este es un contenido de prueba.')
        
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Prueba de Integración')
