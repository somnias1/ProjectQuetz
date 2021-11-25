from rest_framework import serializers
from ..models import Comentario, User, ComentarioComunicado, NotificacionComentario
from datetime import date

from .basicinfo import ComentarioMinimalInfoSerializer


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = (
            "tutorial_padre",
            "fecha_comentario",
            "texto_comentario",
        )

    def create(self, validated_data):
        comentador = self.context["request"].user
        tutorial = validated_data.pop("tutorial_padre")
        instance = super().create(
            {
                **validated_data,
                "tutorial_padre": tutorial,
                "comentador": comentador,
                "fecha_comentario": date.today(),
            }
        )
        notificacion = NotificacionComentario(
            autor=tutorial.autor, tutorial=tutorial, comentario=instance
        )
        notificacion.save()
        return instance


class NotificacionComentarioSerializer(serializers.ModelSerializer):
    comentario = ComentarioMinimalInfoSerializer(read_only=True)

    class Meta:
        model = NotificacionComentario
        fields = (
            "tutorial",
            "comentario",
            "fecha_notificacion",
        )


class ComentarioPlumaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = (
            "id",
            "plumas_comentarios",
        )

    def add_feather(self, user, data):
        infocomentario = Comentario.objects.filter(id=data["comentario"])[0]
        infouser = User.objects.filter(username=user)[0]
        infocomentario.plumas_comentarios.add(infouser)
        return infocomentario

    def remove_feather(self, user, data):
        infocomentario = Comentario.objects.filter(id=data["comentario"])[0]
        infouser = User.objects.filter(username=user)[0]
        infocomentario.plumas_comentarios.remove(infouser)
        return infocomentario


class ComentarioComunicadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentarioComunicado
        fields = (
            "comunicado_padre",
            "fecha_comentario",
            "texto_comentario",
        )

    def create(self, validated_data):
        comentador = self.context["request"].user
        comunicado = validated_data.pop("comunicado_padre")
        instance = super().create(
            {
                **validated_data,
                "comunicado_padre": comunicado,
                "comentador": comentador,
                "fecha_comentario": date.today(),
            }
        )
        return instance
