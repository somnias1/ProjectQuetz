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


class NotificacionComentario(models.Model):
    autor = models.ForeignKey(
        "User", related_name="autor_tutorial_comentado", on_delete=models.CASCADE
    )
    tutorial = models.ForeignKey(
        "Tutorial", related_name="tutorial_comentado", on_delete=models.CASCADE
    )
    comentario = models.ForeignKey(
        "Comentario", related_name="notificacion_comentario", on_delete=models.CASCADE
    )
    fecha_notificacion = models.DateTimeField(auto_now=True)


class NotificacionPlumaComentario(models.Model):
    comentador = models.ForeignKey(
        "User", related_name="%(class)s_comentador", on_delete=models.CASCADE
    )
    comentario = models.ForeignKey(
        "Comentario", related_name="%(class)s_comentario", on_delete=models.CASCADE
    )
    emplumador = models.ForeignKey(
        "User", related_name="%(class)s_emplumador", on_delete=models.CASCADE
    )
    fecha_notificacion = models.DateTimeField(auto_now=True)


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


class NotificacionComentarioComunicado(models.Model):
    comunicador = models.ForeignKey(
        "User",
        related_name="comunicador_comunicado_comentado",
        on_delete=models.CASCADE,
    )
    comunicado = models.ForeignKey(
        "Comunicado", related_name="comunicado_comentado", on_delete=models.CASCADE
    )
    comentario = models.ForeignKey(
        "ComentarioComunicado",
        related_name="notificacion_comentario",
        on_delete=models.CASCADE,
    )
    fecha_notificacion = models.DateTimeField(auto_now=True)
