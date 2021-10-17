from rest_framework import serializers
from ..models import Tutorial, Paso
from .steps import PasoSerializer


class TutorialSerializer(serializers.ModelSerializer):
    paso_Tutorial = PasoSerializer(many=True)

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
        )

    def create(self, validated_data):
        autor = self.context["request"].user
        pasos = validated_data.pop("paso_Tutorial")
        temas = validated_data.pop("temas_tutorial")
        instance = super().create({**validated_data, "autor": autor})
        instance.temas_tutorial.set(temas)
        for paso in pasos:
            Paso.objects.create(tutorial_padre=instance, **paso)

        return instance
