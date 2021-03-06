# Generated by Django 3.2.7 on 2021-11-28 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0047_notificacionplumatutorial"),
    ]

    operations = [
        migrations.CreateModel(
            name="NotificacionPlumaComunicado",
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
                ("fecha_notificacion", models.DateTimeField(auto_now=True)),
                (
                    "comunicado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notificacionplumacomunicado_comunicado",
                        to="api.comunicado",
                    ),
                ),
                (
                    "comunicador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notificacionplumacomunicado_comunicador",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "emplumador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notificacionplumacomunicado_emplumador",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
