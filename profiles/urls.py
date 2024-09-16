from django.urls import path
from . import views


"""
Définit les URL pour l'application 'profiles'.

Ces URL's permettent d'accéder à la vue principale des profils et la vue détaillée pour un profil.
"""

app_name = "profiles"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:username>/", views.profile, name="profile"),
]
