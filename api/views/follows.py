from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import UserFollowing
from ..models import User
from ..serializers import FollowingSerializer


class UserFollowingViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = FollowingSerializer
    queryset = UserFollowing.objects.all()

    def get_serializer_context(self):
        context = super(UserFollowingViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context

