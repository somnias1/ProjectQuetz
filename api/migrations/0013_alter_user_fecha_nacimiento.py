# Generated by Django 3.2.7 on 2021-09-24 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20210924_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.date(2021, 9, 24)),
        ),
    ]
