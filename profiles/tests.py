from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class ProfilesTest(TestCase):

    def setUp(self):
        # Créez les objets nécessaires pour les tests
        self.user = User.objects.create(username="TestUser")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_profiles_index(self):
        # Test de la vue d'index des profils
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>Profiles</title>", response.content)

    def test_profile_detail(self):
        # Test de la vue détaillée d'un profil
        response = self.client.get(reverse("profiles:profile", args=["TestUser"]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>TestUser</title>", response.content)

    def test_profiles_models_str(self):
        # Test de la méthode __str__ des modèles
        self.assertEqual(str(self.profile), self.user.username)
