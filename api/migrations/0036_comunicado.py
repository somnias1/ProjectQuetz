# Generated by Django 3.2.7 on 2021-11-10 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0035_auto_20211110_1842"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comunicado",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "contenido",
                    models.CharField(
                        max_length=255, verbose_name="Titulo del tutorial"
                    ),
                ),
                ("fecha_comunicado", models.DateField(auto_now=True)),
                (
                    "comunicador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comunicado_Usuario",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Comunicado",
                "verbose_name_plural": "Comunicados",
            },
        ),
    ]
