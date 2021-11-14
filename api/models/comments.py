from django.db import models

from .tutorials import Tutorial
from .announces import Comunicado

from .users import User


class Comentario(models.Model):

    tutorial_padre = models.ForeignKey(
        "Tutorial", related_name="%(class)s_Tutorial", on_delete=models.CASCADE
    )
    comentador = models.ForeignKey(
        "User", related_name="%(class)s_Usuario", on_delete=models.CASCADE
    )
    fecha_comentario = models.DateField(auto_now=True)
    texto_comentario = models.TextField(
        "Comentario",
        help_text="Qué tal te ha parecido éste tutorial?",
    )

    plumas_comentarios = models.ManyToManyField("User")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return f"{self.comentador} comentó en {self.tutorial_padre}"


class ComentarioComunicado(models.Model):

    comunicado_padre = models.ForeignKey(
        "Comunicado", related_name="%(class)s_Comunicado", on_delete=models.CASCADE
    )
    comentador = models.ForeignKey(
        "User", related_name="%(class)s_Usuario", on_delete=models.CASCADE
    )
    fecha_comentario = models.DateField(auto_now=True)
    texto_comentario = models.TextField(
        "Comentario",
        help_text="Qué tal te ha parecido éste tutorial?",
    )

    class Meta:
        verbose_name = "Comentario de comunicado"
        verbose_name_plural = "Comentarios de comunicados"

    def __str__(self):
        return f"{self.comentador} comentó el comunicado {self.comunicado_padre}"
