from django.db import models
from .users import User
from datetime import date, datetime


class Comunicado(models.Model):
    comunicador = models.ForeignKey(
        "User", related_name="%(class)s_Usuario", on_delete=models.CASCADE
    )
    contenido = models.CharField("Contenido del comunicado", max_length=255, null=False)
    fecha_comunicado = models.DateField(auto_now=True)
    plumas_comunicados = models.ManyToManyField("User")

    notificacion_creacion = models.ManyToManyField(
        "User",
        related_name="notificacion_creacion_comunicado",
        through="NotificacionCreacionComunicado",
    )

    class Meta:
        verbose_name = "Comunicado"
        verbose_name_plural = "Comunicados"

    def __str__(self):
        return f"Comunicado por {self.comunicador}"


class NotificacionCreacionComunicado(models.Model):
    usuario = models.ForeignKey("User", on_delete=models.CASCADE)
    comunicado = models.ForeignKey("Comunicado", on_delete=models.CASCADE)
    fecha_notificacion = models.DateTimeField(auto_now=True)


class NotificacionPlumaComunicado(models.Model):
    comunicador = models.ForeignKey(
        "User", related_name="%(class)s_comunicador", on_delete=models.CASCADE
    )
    comunicado = models.ForeignKey(
        "Comunicado", related_name="%(class)s_comunicado", on_delete=models.CASCADE
    )
    emplumador = models.ForeignKey(
        "User", related_name="%(class)s_emplumador", on_delete=models.CASCADE
    )
    fecha_notificacion = models.DateTimeField(auto_now=True)
