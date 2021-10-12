from django.db import models
from .tutorials import Tutorial


class Paso(models.Model):
    tutorial_padre = models.ForeignKey(
        "Tutorial", related_name="%(class)s_Tutorial", on_delete=models.CASCADE
    )

    numero_paso = models.IntegerField("Número de paso", null=False, blank=False)
    imagen = models.ImageField(
        "Imagen de referencia (No es obligatoria)", null=True, blank=True, upload_to="steps"
    )
    descripcion = models.TextField(
        "Descripción del paso",
        help_text="Escribe tanto como sea necesario para expresar tu idea",
    )
    adjunto = models.URLField("URL de referencia", null=True, blank=True)

    class Meta:
        verbose_name = "Paso"
        verbose_name_plural = "Pasos"

    def __str__(self):
        return f"Paso {self.paso} del tutorial {self.tutorial_padre}"
