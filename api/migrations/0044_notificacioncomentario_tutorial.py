# Generated by Django 3.2.7 on 2021-11-25 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0043_notificacioncomentario"),
    ]

    operations = [
        migrations.AddField(
            model_name="notificacioncomentario",
            name="tutorial",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tutorial_comentado",
                to="api.tutorial",
            ),
            preserve_default=False,
        ),
    ]
