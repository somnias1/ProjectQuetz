from ..models import User, Tutorial, Comentario, Respuesta

from rest_framework import serializers


class UserBasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "foto_perfil",
        )


class TutorialBasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = (
            "id",
            "titulo",
            "banner",
            "descripcion",
            "nivel",
            "sensible",
            "fecha_creacion",
        )


class RespuestaInfoSerializer(serializers.ModelSerializer):
    comentador_respuesta = UserBasicInfoSerializer(read_only=True)

    class Meta:
        model = Respuesta
        fields = (
            "id",
            "comentador_respuesta",
            "fecha_respuesta",
            "texto_respuesta",
        )


class ComentarioInfoSerializer(serializers.ModelSerializer):
    comentador = UserBasicInfoSerializer(read_only=True)
    respuesta_Comentario = RespuestaInfoSerializer(read_only=True, many=True)

    class Meta:
        model = Comentario
        fields = (
            "id",
            "comentador",
            "fecha_comentario",
            "texto_comentario",
            "respuesta_Comentario",
        )
