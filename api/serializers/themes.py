from rest_framework import serializers
from ..models import Tema


class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = ("categoria_tema", "nombre_tema", "imagen_tema")
