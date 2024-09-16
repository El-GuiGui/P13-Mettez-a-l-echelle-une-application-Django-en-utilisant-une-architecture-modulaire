from django.db import migrations, models
from django.contrib.auth.models import User


class Migration(migrations.Migration):
    """
    Migration pour créer le modèle 'Profile' et associer une table existante.

    Cette migration ne crée pas la table en base de données, mais définit l'état du modèle 'Profile' avec les champs suivants:
    - id: Clé primaire auto-incrémentée.
    - favorite_city: Champ de type CharField pour stocker la ville préférée de l'utilisateur.
    - user: Relation OneToOne avec le modèle User, supprimée en cascade si l'utilisateur est supprimé.

    La table associée à ce modèle est 'oc_lettings_site_profile'.
    """

    initial = True

    dependencies = [
        ("auth", "0011_update_proxy_permissions"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="Profile",
                    fields=[
                        (
                            "id",
                            models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                        ),
                        ("favorite_city", models.CharField(max_length=64, blank=True)),
                        ("user", models.OneToOneField(on_delete=models.CASCADE, to="auth.User")),
                    ],
                    options={
                        "db_table": "oc_lettings_site_profile",
                    },
                ),
            ],
            database_operations=[],
        ),
    ]
