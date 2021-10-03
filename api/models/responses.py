from django.db import models

from .users import User
from .comments import Comentario


class Respuesta(models.Model):

    comentariopadre = models.ForeignKey(
        "Comentario", related_name="%(class)s_Comentario", on_delete=models.CASCADE
    )
    comentadorrespuesta = models.ForeignKey(
        "User", related_name="%(class)s_Usuario", on_delete=models.CASCADE
    )
    fecha_respuesta = models.DateField(auto_now=True)
    texto_respuesta = models.TextField(
        "Respuesta",
        help_text="Algo que decir de éste comentario?",
    )

    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"

    def __str__(self):
        return (
            f"{self.comentadorrespuesta} respondió al comentario {self.comentariopadre}"
        )
