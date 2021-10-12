from rest_framework import serializers
from ..models import Paso, Tutorial
#from .steps import PasosSerializer


class PasoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paso
        fields = ("numero_paso", "imagen", "descripcion", "adjunto")

    def create(self, validated_data):
        #print(dir(self.context["request"]._request))
        path = self.context["request"]._request.path
        print(path)
        tutorial = path.find("tutorials/")
        print(tutorial)
        steps = path.find("/steps", tutorial)
        print(steps)
        cont = int(path[tutorial+10:steps])
        print(cont)
        tutorial_padre=Tutorial.objects.filter(id=cont).first()
        #print(validated_data)
        objeto = super().create({**validated_data,"tutorial_padre":tutorial_padre})
        if objeto:
            return objeto
        raise serializers.ValidationError({"Error":"Información inválida"})