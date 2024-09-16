from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration de l'application 'profiles'.

    Attributes:
        default_auto_field: Définit le type de champ auto-incrémenté par défaut pour les modèles.
        name: Le nom de l'application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"
