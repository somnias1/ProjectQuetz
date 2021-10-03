from django.db import models

from .tutorials import Tutorial


class Comentario(models.Model):

    tutorialpadre = models.ForeignKey(
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

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return f"{self.comentador} comentó en {self.tutorialpadre}"
