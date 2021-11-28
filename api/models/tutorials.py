from django.db import models
from .users import User
from .themes import Tema
from datetime import date, datetime


class Tutorial(models.Model):

    niveles = [
        ("bas", "Básico"),
        ("med", "Intermedio"),
        ("adv", "Avanzado"),
    ]

    autor = models.ForeignKey(
        "User", related_name="%(class)s_Usuario", on_delete=models.CASCADE
    )

    titulo = models.CharField("Titulo del tutorial", max_length=255, null=False)
    banner = models.ImageField(blank=False, upload_to="tutorials")
    descripcion = models.CharField(
        "Descripción del tutorial",
        help_text="Un texto corto que indique la intención de tu tutorial",
        max_length=255,
        null=False,
    )
    nivel = models.CharField(
        "Dificultad del tutorial", choices=niveles, null=False, max_length=32
    )
    sensible = models.BooleanField(
        help_text="Es tu tutorial apto para todos?", default=False
    )

    temas_tutorial = models.ManyToManyField("Tema")
    plumas_tutoriales = models.ManyToManyField("User")

    fecha_creacion = models.DateField(auto_now=True)

    notificacion_creacion = models.ManyToManyField(
        "User",
        related_name="notificacion_creacion_tutorial",
        through="NotificacionCreacionTutorial",
    )

    class Meta:
        verbose_name = "Tutorial"
        verbose_name_plural = "Tutoriales"

    def __str__(self):
        return f"{self.titulo} por {self.autor}"


class NotificacionCreacionTutorial(models.Model):
    usuario = models.ForeignKey("User", on_delete=models.CASCADE)
    tutorial = models.ForeignKey("Tutorial", on_delete=models.CASCADE)
    fecha_notificacion = models.DateTimeField(auto_now=True)


class NotificacionPlumaTutorial(models.Model):
    autor = models.ForeignKey(
        "User", related_name="%(class)s_autor", on_delete=models.CASCADE
    )
    tutorial = models.ForeignKey(
        "Tutorial", related_name="%(class)s_tutorial", on_delete=models.CASCADE
    )
    emplumador = models.ForeignKey(
        "User", related_name="%(class)s_emplumador", on_delete=models.CASCADE
    )
    fecha_notificacion = models.DateTimeField(auto_now=True)
