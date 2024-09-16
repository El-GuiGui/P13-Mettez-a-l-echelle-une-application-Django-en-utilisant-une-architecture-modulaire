from django.contrib import admin
from django.urls import path, include
from . import views


"""
Définit les URL pour l'application principale.

Ce module établit les chemins d'URL utilisés par l'application, y compris les
lettings, les profils et l'interface d'administration.

Routes:
    - "": La page d'accueil, gérée par la fonction `index` dans `views`.
    - "lettings/": Redirige vers les URLs de l'application 'lettings'.
    - "profiles/": Redirige vers les URLs de l'application 'profiles'.
    - "admin/": Accède à l'interface d'administration de Django.
    - "trigger-error/": La page qui génère une erreur 500,
    fonction trigger_error dans view pour tester la validité de la page erreur.
"""

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("admin/", admin.site.urls),
    path("trigger-error/", views.trigger_error, name="trigger_error"),
]
