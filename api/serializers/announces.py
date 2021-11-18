from rest_framework import serializers
from ..models import Comunicado, User
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
        return instance


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
