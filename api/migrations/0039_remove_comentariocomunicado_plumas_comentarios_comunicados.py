# Generated by Django 3.2.7 on 2021-11-14 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0038_comentariocomunicado"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comentariocomunicado",
            name="plumas_comentarios_comunicados",
        ),
    ]
