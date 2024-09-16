from django.test import TestCase
from django.urls import reverse


class OCLettingsSiteViewsTest(TestCase):
    def test_index_view(self):
        # Test de la vue d'index de l'application principale
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>Holiday Homes</title>", response.content)

    def test_error_404_view(self):
        # Test de la page 404 personnalisée
        response = self.client.get("/non-existent-url/")
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"<h1>404 - Page Not Found</h1>", response.content)

    def test_trigger_error_view(self):
        # Test pour déclencher l'erreur 500 via la vue dédiée
        with self.assertRaises(ValueError):
            self.client.get(reverse("trigger_error"))
