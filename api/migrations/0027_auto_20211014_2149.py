# Generated by Django 3.2.7 on 2021-10-14 21:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20211012_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temausuario',
            name='tema',
        ),
        migrations.RemoveField(
            model_name='temausuario',
            name='usuario',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='temas_tutorial',
            field=models.ManyToManyField(to='api.Tema'),
        ),
        migrations.AddField(
            model_name='user',
            name='temas_seguidos',
            field=models.ManyToManyField(to='api.Tema'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.date(2021, 10, 14)),
        ),
        migrations.DeleteModel(
            name='TemaTutorial',
        ),
        migrations.DeleteModel(
            name='TemaUsuario',
        ),
    ]
