from django.contrib import admin

from .models import Letting
from .models import Address

# Enregistre les modèles Letting et Address dans l'interface d'administration de Django.
admin.site.register(Letting)
admin.site.register(Address)
