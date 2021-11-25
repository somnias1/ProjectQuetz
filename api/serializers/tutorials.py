from rest_framework import serializers
from ..models import Tutorial, Paso, User, NotificacionCreacionTutorial
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

        lista_seguidores = autor.followers.values_list("user_id", flat=True)
        seguidores = User.objects.filter(id__in=lista_seguidores)
        instance.notificacion_creacion.add(*seguidores)

        return instance


class TutorialSerializer(serializers.ModelSerializer):
    autor = UserBasicInfoSerializer(read_only=True)
    temas_tutorial = TemaSerializer(read_only=True, many=True)

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
            "plumas_tutoriales",
        )


class TutorialMinimalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ("id", "autor", "titulo")


class TutorialNotificacionCreacionSerializer(serializers.ModelSerializer):
    tutorial = TutorialMinimalInfoSerializer(read_only=True)

    class Meta:
        model = NotificacionCreacionTutorial
        fields = (
            "tutorial",
            "tutorial",
            "fecha_notificacion",
        )


class TutorialRetrieveSerializer(serializers.ModelSerializer):
    paso_Tutorial = PasoSerializer(many=True)
    autor = UserBasicInfoSerializer(read_only=True)
    comentario_Tutorial = ComentarioInfoSerializer(many=True, read_only=True)
    temas_tutorial = TemaSerializer(read_only=True, many=True)

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
            "plumas_tutoriales",
            "paso_Tutorial",
            "comentario_Tutorial",
            "fecha_creacion",
        )


class TutorialPlumaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = (
            "id",
            "plumas_tutoriales",
        )

    def add_feather(self, user, data):
        infotutorial = Tutorial.objects.filter(id=data["tutorial"])[0]
        infouser = User.objects.filter(username=user)[0]
        infotutorial.plumas_tutoriales.add(infouser)
        return infotutorial

    def remove_feather(self, user, data):
        infotutorial = Tutorial.objects.filter(id=data["tutorial"])[0]
        infouser = User.objects.filter(username=user)[0]
        infotutorial.plumas_tutoriales.remove(infouser)
        return infotutorial
