import os
import sys


def main():
    """
    Configure l'environnement Django et exécute les commandes de gestion.

    Définit la variable d'environnement des paramètres Django, puis tente
    d'importer et d'exécuter 'execute_from_command_line' pour traiter les
    commandes de la ligne de commande.

    Raises:
        ImportError: Si Django n'est pas installé ou n'est pas disponible dans
        le PYTHONPATH, une exception est levée.

    Returns:
        None
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
