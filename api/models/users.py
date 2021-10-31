from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from datetime import timedelta, date
from django.utils import timezone
from .themes import Tema


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=86)
    USERNAME_FIELD = "username"
    lista_idiomas = [
        ("en", "Inglés"),
        ("es", "Español"),
        ("fr", "Francés"),
        ("de", "Alemán"),
        ("cn", "Chino"),
        ("jp", "Japonés"),
        ("it", "Italiano"),
        ("pt", "Portugués"),
    ]

    email = models.EmailField("Correo", null=False)
    fecha_registro = models.DateField(auto_now=True)
    fecha_nacimiento = models.DateField(null=False, default=timezone.now)
    institucion_educativa = models.CharField(null=True, blank=True, max_length=255)
    idiomas = MultiSelectField(
        null=True,
        blank=True,
        choices=lista_idiomas,
        max_choices=len(lista_idiomas),
        max_length=len(lista_idiomas),
    )
    ubicacion = models.CharField(null=True, blank=True, max_length=255)
    facebookurl = models.URLField("Enlace a Facebook", null=True, blank=True)
    instagramurl = models.URLField("Enlace a Instagram", null=True, blank=True)
    twitterurl = models.URLField("Enlace a Twitter", null=True, blank=True)
    youtubeurl = models.URLField("Enlace a Youtube", null=True, blank=True)
    adulto = models.BooleanField(default=False)
    foto_perfil = models.ImageField(
        null=True,
        blank=True,
        upload_to="users",
    )
    temas_seguidos = models.ManyToManyField("Tema")

    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"{self.username}"
