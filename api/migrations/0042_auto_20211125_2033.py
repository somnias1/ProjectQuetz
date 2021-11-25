# Generated by Django 3.2.7 on 2021-11-25 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_auto_20211124_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificacionCreacionComunicado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_notificacion', models.DateTimeField(auto_now=True)),
                ('comunicado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.comunicado')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comunicado',
            name='notificacion_creacion',
            field=models.ManyToManyField(related_name='notificacion_creacion_comunicado', through='api.NotificacionCreacionComunicado', to=settings.AUTH_USER_MODEL),
        ),
    ]