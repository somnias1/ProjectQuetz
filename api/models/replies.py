from django.db import models

from .users import User
from .comments import Comentario


class Respuesta(models.Model):

    comentario_padre = models.ForeignKey(
        "Comentario", related_name="%(class)s_Comentario", on_delete=models.CASCADE
    )
    comentador_respuesta = models.ForeignKey(
        "User", related_name="%(class)s_Usuario", on_delete=models.CASCADE
    )
    fecha_respuesta = models.DateField(auto_now=True)
    texto_respuesta = models.TextField(
        "Respuesta",
        help_text="Algo que decir de éste comentario?",
    )

    notificacion_reacion = models.ManyToManyField(
        "User",
        related_name="notificacion_creacion_respuesta",
        through="NotificacionRespuesta",
    )

    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"

    def __str__(self):
        return f"{self.comentador_respuesta} respondió al comentario {self.comentario_padre}"


class NotificacionRespuesta(models.Model):
    comentador = models.ForeignKey(
        "User", related_name="comentador_comentario", on_delete=models.CASCADE
    )
    tutorial = models.ForeignKey(
        "Tutorial",
        related_name="tutorial_comentado_respondido",
        on_delete=models.CASCADE,
    )
    comentario = models.ForeignKey(
        "Comentario", related_name="comentario_respondido", on_delete=models.CASCADE
    )

    respuesta = models.ForeignKey(
        "Respuesta", related_name="notificacion_respuesta", on_delete=models.CASCADE
    )
    fecha_notificacion = models.DateTimeField(auto_now=True)
