from django.db import models

# from django.core.validators import MaxValueValidator, MinLengthValidator
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Représente le profil d'un utilisateur.

    Attributes:
        user (OneToOneField): Référence à l'utilisateur lié à ce profil.
        favorite_city (CharField): La ville préférée de l'utilisateur.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne du profil, basée sur le nom d'utilisateur.

        Returns:
            str: Le nom d'utilisateur associé au profil.
        """
        return self.user.username

    class Meta:
        """
        Métadonnées pour le modèle Profile.

        Attributes:
            db_table (str): Le nom de la table de la base de données associée à ce modèle.
        """

        db_table = "oc_lettings_site_profile"
