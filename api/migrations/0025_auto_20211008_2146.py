# Generated by Django 3.2.7 on 2021-10-08 21:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0024_auto_20211003_1652"),
    ]

    operations = [
        migrations.RenameField(
            model_name="paso",
            old_name="paso",
            new_name="numero_paso",
        ),
        migrations.AlterField(
            model_name="user",
            name="fecha_nacimiento",
            field=models.DateField(default=datetime.date(2021, 10, 8)),
        ),
    ]
