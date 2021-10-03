from django.db import models

from .users import User
from .tutorials import Tutorial


class Pluma(models.Model):
    user = models.ForeignKey(
        "User", related_name="%(class)s_Usuario", on_delete=models.CASCADE
    )
    tutorial = models.ForeignKey(
        "Tutorial", related_name="%(class)s_Tutorial", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Pluma"
        verbose_name_plural = "Plumas"

    def __str__(self):
        return f"A {self.user} le gusta {self.tutorial}"
