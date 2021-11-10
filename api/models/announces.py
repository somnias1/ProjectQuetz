from django.db import models
from .users import User
from datetime import date


class Comunicado(models.Model):
    # user, content, date
    comunicador = models.ForeignKey(
        "User", related_name="%(class)s_Usuario", on_delete=models.CASCADE
    )
    contenido = models.CharField("Titulo del tutorial", max_length=255, null=False)
    fecha_comunicado = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Comunicado"
        verbose_name_plural = "Comunicados"

    def __str__(self):
        return f"Comunicado por {self.comunicador}"
