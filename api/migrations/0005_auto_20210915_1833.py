# Generated by Django 3.2.7 on 2021-09-15 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_user_fecha_nacimiento"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="correo",
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]
