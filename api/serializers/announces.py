from rest_framework import serializers
from ..models import Comunicado, User, NotificacionCreacionComunicado
from datetime import date

from .basicinfo import UserBasicInfoSerializer, ComentarioComunicadoInfoSerializer


class ComunicadoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunicado
        fields = (
            "contenido",
            "fecha_comunicado",
        )

    def create(self, validated_data):
        comunicador = self.context["request"].user
        instance = super().create(
            {
                **validated_data,
                "comunicador": comunicador,
                "fecha_comunicado": date.today(),
            }
        )

        lista_seguidores = comunicador.followers.values_list("user_id", flat=True)
        seguidores = User.objects.filter(id__in=lista_seguidores)
        instance.notificacion_creacion.add(*seguidores)

        return instance


class ComunicadorMinimalInfoSerializer(serializers.ModelSerializer):
    comunicador = UserBasicInfoSerializer(read_only=True)

    class Meta:
        model = Comunicado
        fields = ("id", "comunicador")


class ComunicadoNotificacionCreacionSerializer(serializers.ModelSerializer):
    comunicado = ComunicadorMinimalInfoSerializer(read_only=True)

    class Meta:
        model = NotificacionCreacionComunicado
        fields = (
            "comunicado",
            "fecha_notificacion",
        )


class ComunicadoSerializer(serializers.ModelSerializer):
    comunicador = UserBasicInfoSerializer(read_only=True)
    comentariocomunicado_Comunicado = ComentarioComunicadoInfoSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = Comunicado
        fields = (
            "id",
            "comunicador",
            "contenido",
            "fecha_comunicado",
            "plumas_comunicados",
            "comentariocomunicado_Comunicado",
        )


class ComunicadoPlumaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunicado
        fields = (
            "id",
            "plumas_comunicados",
        )

    def add_feather(self, user, data):
        infocomunicado = Comunicado.objects.filter(id=data["comunicado"])[0]
        infouser = User.objects.filter(username=user)[0]
        infocomunicado.plumas_comunicados.add(infouser)
        return infocomunicado

    def remove_feather(self, user, data):
        infocomunicado = Comunicado.objects.filter(id=data["comunicado"])[0]
        infouser = User.objects.filter(username=user)[0]
        infocomunicado.plumas_comunicados.remove(infouser)
        return infocomunicado
