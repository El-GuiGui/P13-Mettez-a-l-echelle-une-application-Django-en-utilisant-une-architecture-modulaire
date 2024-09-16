from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class LettingsTest(TestCase):

    def setUp(self):
        # Créatuon des objets nécessaires pour les tests
        self.address = Address.objects.create(
            number=2,
            street="test street",
            city="test city",
            state="test state",
            zip_code=10100,
            country_iso_code="FRA",
        )
        self.letting = Letting.objects.create(title="Test Letting", address=self.address)

    def test_lettings_index(self):
        # Test de la vue d'index des locations
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>Lettings</title>", response.content)

    def test_letting_detail(self):
        # Test de la vue détaillée d'une location
        response = self.client.get(reverse("lettings:letting", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>Test Letting</title>", response.content)

    def test_lettings_models_str(self):
        # Test de la méthode __str__ des modèles
        self.assertEqual(str(self.address), f"{self.address.number} {self.address.street}")
        self.assertEqual(str(self.letting), self.letting.title)
