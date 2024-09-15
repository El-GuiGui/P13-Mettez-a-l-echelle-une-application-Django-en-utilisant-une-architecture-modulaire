from django.db import migrations, models
from django.contrib.auth.models import User


class Migration(migrations.Migration):

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
