from django.db import models


class Tema(models.Model):

    categorias = [
        ("instmsc", "Instrumento musical"),
        ("tmsc", "Teoría musical"),
        ("prgm", "Programación"),
        ("dbj", "Dibujo"),
        ("art", "Artesanías"),
        ("mnga", "Manga - Anime"),
        ("ltr", "Literatura"),
        ("coci", "Cocina"),
        ("mrk", "Marketing"),
        ("dsgn", "Diseño"),
        ("otrs", "Otros")
    ]
    categoria_tema = models.CharField(choices=categorias, null=False, max_length=32)
    nombre_tema = models.CharField(
        "Nombre del tema", unique=True, null=False, max_length=128
    )
    imagen_tema = models.ImageField(null=False, upload_to="themes")

    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = "Temas"

    def __str__(self):
        return f"{self.nombre_tema}"
