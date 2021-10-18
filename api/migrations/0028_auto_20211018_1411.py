# Generated by Django 3.2.7 on 2021-10-18 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0027_auto_20211014_2149"),
    ]

    operations = [
        migrations.AddField(
            model_name="tutorial",
            name="fecha_creacion",
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="fecha_nacimiento",
            field=models.DateField(default=datetime.date(2021, 10, 18)),
        ),
    ]
