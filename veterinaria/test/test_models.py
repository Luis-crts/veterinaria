from django.test import TestCase
from veterinaria.modelos import Publicacion

class PublicacionModelTest(TestCase):
    def test_crear_publicacion(self):
        publicacion = Publicacion.objects.create(
            titulo="Prueba de título",
            contenido="Contenido de prueba",
        )
        self.assertEqual(publicacion.titulo, "Prueba de título")
