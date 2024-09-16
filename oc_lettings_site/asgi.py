import os

from django.core.asgi import get_asgi_application

# Configuration du module ASGI pour le projet Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

application = get_asgi_application()
