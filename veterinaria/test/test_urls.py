from django.test import SimpleTestCase
from django.urls import reverse, resolve
from veterinaria.views import index

class TestUrls(SimpleTestCase):
    def test_index_url_resuelve(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)
