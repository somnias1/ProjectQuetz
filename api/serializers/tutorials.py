from rest_framework import serializers
from ..models import Tutorial
from .steps import PasoSerializer


class TutorialSerializer(serializers.ModelSerializer):
    paso_Tutorial = PasoSerializer(many=True, read_only=True)

    class Meta:
        model = Tutorial
        fields = (
            "autor",
            "titulo",
            "banner",
            "descripcion",
            "nivel",
            "sensible",
            "paso_Tutorial",
        )

    def create(self, validated_data):
        autor = self.context["request"].user
        objeto = super().create({**validated_data, "autor": autor})
        return objeto

    """def get_autor(self, obj):
        user = self.context['request'].user
        print(user)
        return user"""
