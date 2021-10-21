from rest_framework import serializers
from ..models import Comentario, User
from datetime import date
#from .tutorials import UserBasicInfoSerializer


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
        return instance

class UserCommentBasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "foto_perfil",
        )
        
class ComentarioInfoSerializer(serializers.ModelSerializer):
    comentador = UserCommentBasicInfoSerializer(read_only = True)
    class Meta:
        model = Comentario
        fields = (
            "id",
            "comentador",
            "fecha_comentario",
            "texto_comentario",
        )

