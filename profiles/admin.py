from django.contrib import admin

from .models import Profile


# Enregistre le modèle Profile dans l'interface d'administration de Django.
admin.site.register(Profile)
