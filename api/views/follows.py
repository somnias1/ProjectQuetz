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


"""
    @action(detail=False, methods=["post"])
    def follow(self, username):
        if (
            # Si no existe el usuario o si no se proporcionó un usuario
            not username.GET.get("username")
            or not User.objects.filter(
                username=self.username.GET.get("username")
            ).exists()
        ):
            return Response(
                {"Error": "Username inválido"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = UserSerializer
        usuario = User.objects.filter(id=self.request.id)[0]
        usuario_objetivo = User.objects.get(username=username)
        usuario.following.add(usuario_objetivo)
        return Response({"Exito": "Usuario seguido"}, status=status.HTTP_200_OK)"""
