from rest_framework import serializers
from ..models import Comentario, User, Respuesta
from datetime import date


class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = (
            "comentario_padre",
            "fecha_respuesta",
            "texto_respuesta",
        )

    def create(self, validated_data):
        comentador_respuesta = self.context["request"].user
        comentario = validated_data.pop("comentario_padre")
        instance = super().create(
            {
                **validated_data,
                "comentario_padre": comentario,
                "comentador_respuesta": comentador_respuesta,
                "fecha_respuesta": date.today(),
            }
        )
        return instance
