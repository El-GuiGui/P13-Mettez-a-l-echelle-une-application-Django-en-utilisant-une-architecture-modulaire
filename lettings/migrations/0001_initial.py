from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Migration pour créer les modèles 'Letting' et 'Address' et associer des tables existantes.

    Cette migration ne crée pas les tables en base de données, mais définit l'état des modèles 'Letting' et 'Address' avec les champs suivants :

    - Letting:
      - id: Clé primaire auto-incrémentée.
      - title: Champ de type CharField pour stocker le titre du logement.
      - address: Relation OneToOne avec le modèle 'Address', supprimée en cascade si l'adresse est supprimée.
      - La table associée à ce modèle est 'oc_lettings_site_letting'.

    - Address:
      - id: Clé primaire auto-incrémentée.
      - number: Champ de type PositiveIntegerField pour le numéro de l'adresse.
      - street: Champ de type CharField pour le nom de la rue.
      - city: Champ de type CharField pour la ville.
      - state: Champ de type CharField pour l'état (2 caractères).
      - zip_code: Champ de type PositiveIntegerField pour le code postal.
      - country_iso_code: Champ de type CharField pour le code ISO du pays (3 caractères).
      - La table associée à ce modèle est 'oc_lettings_site_address'.
    """

    initial = True

    dependencies = []

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="Letting",
                    fields=[
                        (
                            "id",
                            models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                        ),
                        ("title", models.CharField(max_length=256)),
                        ("address", models.OneToOneField(on_delete=models.CASCADE, to="lettings.Address")),
                    ],
                    options={
                        "db_table": "oc_lettings_site_letting",
                    },
                ),
            ],
            database_operations=[],
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="Address",
                    fields=[
                        (
                            "id",
                            models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                        ),
                        ("number", models.PositiveIntegerField()),
                        ("street", models.CharField(max_length=64)),
                        ("city", models.CharField(max_length=64)),
                        ("state", models.CharField(max_length=2)),
                        ("zip_code", models.PositiveIntegerField()),
                        ("country_iso_code", models.CharField(max_length=3)),
                    ],
                    options={
                        "db_table": "oc_lettings_site_address",
                    },
                ),
            ],
            database_operations=[],
        ),
    ]
