from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Configuration de l'application 'lettings'.

    Attributs:
        default_auto_field: Définit le type de clé primaire par défaut pour les modèles de l'app.
        name: Nom de l'application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "lettings"
