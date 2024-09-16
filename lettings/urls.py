from django.urls import path
from . import views

"""
Configuration des URLs pour l'application 'lettings'.


Routes disponibles :
    "" : Affiche la liste de toutes les locations.
    "<int:letting_id>/" : Affiche les détails d'une location spécifique identifiée par son ID.
"""

app_name = "lettings"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
