from rest_framework import serializers
from ..models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
    #autor = serializers.IntegerField(default=-1)

    class Meta:
        model = Tutorial
        fields = ("titulo", "banner", "descripcion", "nivel", "sensible")

    def create(self, validated_data):
        autor = self.context['request'].user
        objeto = super().create({**validated_data, "autor": autor})
        return objeto


    """def get_autor(self, obj):
        user = self.context['request'].user
        print(user)
        return user"""
