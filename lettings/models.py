from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator

# from django.contrib.auth.models import User


class Address(models.Model):
    """
    Représente une adresse avec les détails :
    le numéro, la rue, la ville, l'état, le code postal, et le code ISO du pays.

    Attributes:
        number (PositiveIntegerField): Le numéro de l'adresse, limité à 4 chiffres.
        street (CharField): Le nom de la rue, jusqu'à 64 caractères.
        city (CharField): Le nom de la ville, jusqu'à 64 caractères.
        state (CharField): L'état, doit être exactement 2 caractères.
        zip_code (PositiveIntegerField): Le code postal, limité à 5 chiffres.
        country_iso_code (CharField): Le code ISO du pays, doit être exactement 3 caractères.


    Meta:
        db_table (str): Nom de la table associée à ce modèle dans la base de données.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f"{self.number} {self.street}"

    class Meta:
        db_table = "oc_lettings_site_address"
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Représente une location liée à une adresse.

    Attributes:
        title (CharField): Le titre de la location, jusqu'à 256 caractères.
        address (OneToOneField): La relation unique vers un objet Address.

    Meta:
        db_table (str): Nom de la table associée à ce modèle dans la base de données.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "oc_lettings_site_letting"
