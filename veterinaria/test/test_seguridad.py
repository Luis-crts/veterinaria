from django.test import TestCase
from veterinaria.modelos import Publicacion

class SeguridadTest(TestCase):
    def test_inyeccion_sql(self):
        with self.assertRaises(Exception):
            Publicacion.objects.raw("SELECT * FROM veterinaria_publicacion WHERE id = '1 OR 1=1'")
    
    def test_proteccion_csrf(self):
        response = self.client.post('/añadir/', {'nombre': 'Test'}, follow=True)
        self.assertContains(response, "CSRF verification failed", status_code=403)
