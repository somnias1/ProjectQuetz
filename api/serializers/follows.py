from rest_framework import serializers
from ..models import UserFollowing


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ("user_id", "following_user_id", "getfollowingusername", "created")


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ("getbasicusername", "created")
