from django.db import models
from .users import User
from .tutorials import Tutorial


class TemaTutorial(models.Model):
    tutorial = models.ForeignKey(
        "Tutorial", related_name="%(class)s_Tutorial", on_delete=models.CASCADE
    )
    tema = models.ForeignKey(
        "Tema", related_name="%(class)s_Tema", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Tema del tutorial"
        verbose_name_plural = "Temas del tutorial"

    def __str__(self):
        return f"{self.tutorial} tiene el tema {self.tema}"
