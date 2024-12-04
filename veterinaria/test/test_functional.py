from django.test import TestCase
from django.urls import reverse
from veterinaria.modelos import Publicacion

class PruebaFuncional(TestCase):
    def test_agregar_y_listar_publicacion(self):
        datos_formulario = {
            'nombre': 'Nueva Publicación',
            'descripcion': 'Contenido de prueba para la nueva publicación.',
            'categoria': 'gato',
            'edad': '2 años',
            'estado_vacuna': '1',
            'duracion_pipeta': '3'
        }
        response = self.client.post(reverse('añadir_paciente'), data=datos_formulario)
        self.assertEqual(response.status_code, 302)

        self.assertEqual(Publicacion.objects.count(), 1)
        publicacion = Publicacion.objects.first()
        self.assertEqual(publicacion.nombre, 'Nueva Publicación')

        response = self.client.get(reverse('lista_gatos'))
        self.assertContains(response, 'Nueva Publicación')
        self.assertContains(response, 'Contenido de prueba para la nueva publicación.')
