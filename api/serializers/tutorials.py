from rest_framework import serializers
from ..models import Tutorial, Paso, User
from .steps import PasoSerializer
from datetime import date

from .basicinfo import UserBasicInfoSerializer, ComentarioInfoSerializer
from .themes import TemaSerializer


class TutorialDetailSerializer(serializers.ModelSerializer):
    paso_Tutorial = PasoSerializer(many=True)

    class Meta:
        model = Tutorial
        fields = (
            "titulo",
            "banner",
            "descripcion",
            "nivel",
            "sensible",
            "temas_tutorial",
            "paso_Tutorial",
            "fecha_creacion",
        )

    def create(self, validated_data):
        autor = self.context["request"].user
        pasos = validated_data.pop("paso_Tutorial")
        temas = validated_data.pop("temas_tutorial")
        instance = super().create(
            {**validated_data, "autor": autor, "fecha_creacion": date.today()}
        )
        instance.temas_tutorial.set(temas)
        for paso in pasos:
            Paso.objects.create(tutorial_padre=instance, **paso)

        return instance


class TutorialSerializer(serializers.ModelSerializer):
    autor = UserBasicInfoSerializer(read_only=True)
    temas_tutorial = TemaSerializer(read_only=True, many = True)

    class Meta:
        model = Tutorial
        fields = (
            "id",
            "autor",
            "titulo",
            "banner",
            "descripcion",
            "nivel",
            "sensible",
            "temas_tutorial",
            "fecha_creacion",
        )


class TutorialRetrieveSerializer(serializers.ModelSerializer):
    paso_Tutorial = PasoSerializer(many=True)
    autor = UserBasicInfoSerializer(read_only=True)
    comentario_Tutorial = ComentarioInfoSerializer(many=True, read_only=True)
    temas_tutorial = TemaSerializer(read_only=True, many = True)

    class Meta:
        model = Tutorial
        fields = (
            "autor",
            "titulo",
            "banner",
            "descripcion",
            "nivel",
            "sensible",
            "temas_tutorial",
            "paso_Tutorial",
            "comentario_Tutorial",
            "fecha_creacion",
        )
