from django.db import models
from .users import User
from .themes import Tema


class TemaUsuario(models.Model):
    usuario = models.ForeignKey(
        "User", related_name="Usuario", on_delete=models.CASCADE
    )
    tema = models.ForeignKey("Tema", related_name="Tema", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Tema seguido por el usuario"
        verbose_name_plural = "Temas seguidos por el usuario"

    def __str__(self):
        return f"{self.usuario} sigue el tema {self.tema}"
