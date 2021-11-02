from rest_framework import serializers
from ..models import UserFollowing
from .basicinfo import UserBasicInfoSerializer


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = (
            "following_user_id",
            # "getfollowingusername",
            "created",
        )

    def create(self, validated_data):
        user = self.context["request"].user
        instance = super().create({**validated_data, "user_id": user})

        return instance


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ("getbasicusername", "created")
