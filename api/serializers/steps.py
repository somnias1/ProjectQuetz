from rest_framework import serializers
from ..models import Paso, Tutorial


class PasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paso
        fields = ("numero_paso", "imagen", "descripcion", "adjunto")

    def create(self, validated_data):
        path = self.context["request"]._request.path
        tutorial = path.find("tutorials/")
        steps = path.find("/steps", tutorial)
        cont = int(path[tutorial + 10 : steps])
        tutorial_padre = Tutorial.objects.filter(id=cont).first()
        objeto = super().create({**validated_data, "tutorial_padre": tutorial_padre})
        if objeto:
            return objeto
        raise serializers.ValidationError({"Error": "Información inválida"})
