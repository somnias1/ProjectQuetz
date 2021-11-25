from rest_framework import serializers
from ..models import UserFollowing, User
from .basicinfo import UserBasicInfoSerializer


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = (
            "following_user_id",
            "created",
        )

    def create(self, validated_data):
        user = self.context["request"].user
        instance = super().create({**validated_data, "user_id": user})

        return instance


class FollowersSerializer(serializers.ModelSerializer):
    user_id = UserBasicInfoSerializer(read_only=True)

    class Meta:
        model = UserFollowing
        fields = ("user_id", "created")
