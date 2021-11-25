from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    AllowAny,
    IsAuthenticated,
)

from ..serializers import (
    UserLoginSerializer,
    UserSerializer,
    UserSignUpSerializer,
    UserProfileUpdateSerializer,
    UserNotificacionSerializer,
    TutorialNotificacionCreacionSerializer,
)

from ..models import User, NotificacionCreacionTutorial
from datetime import date, timedelta, datetime

# Serializador general para usuarios
class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    # Acción a realizar, login
    @permission_classes([AllowAny])
    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {"user": UserSerializer(user).data, "access_token": token}

        # Cambia la última vez que inició sesión
        data["user"]["last_login"] = datetime.today()

        # Lee la edad del usuario que inicia sesión con el fin de validar
        # Si ya es mayor de edad en caso de que no lo fuera

        return Response(data, status=status.HTTP_201_CREATED)

    @permission_classes([AllowAny])
    @action(detail=False, methods=["post"])
    def signup(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        token = Token.objects.get_or_create(user=user)[0].key
        data = {"user": UserSerializer(user).data, "access_token": token}

        return Response(data, status=status.HTTP_201_CREATED)

    @permission_classes([IsAuthenticated])
    @action(detail=False, methods=["get"])
    def profile(self, request):
        if not User.objects.filter(username=self.request.user).exists():
            return Response(
                {"Error": "Requiere sesión activa"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = UserSerializer()
        specificuser = serializer.get_specific_user(request.user)

        return Response(specificuser.data, status=status.HTTP_200_OK)

    @permission_classes([IsAuthenticated])
    @action(detail=False, methods=["patch"])
    def profileupdate(self, request):
        if not User.objects.filter(username=self.request.user).exists():
            return Response(
                {"Error": "Requiere sesión activa"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = UserProfileUpdateSerializer()
        serializer.update_profile(request.user, request.data)
        return Response(
            {"Exito": "Perfil actualizado correctamente"}, status=status.HTTP_200_OK
        )

    @permission_classes([AllowAny])
    @action(detail=False, methods=["get"])
    def watch(self, request):
        if (
            # Si no existe el usuario o si no se proporcionó un usuario
            not request.GET.get("username")
            or not User.objects.filter(
                username=self.request.GET.get("username")
            ).exists()
        ):
            return Response(
                {"Error": "Username inválido"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = UserSerializer()
        specificuser = serializer.get_specific_user(request.GET["username"])

        return Response(specificuser.data, status=status.HTTP_200_OK)

    @permission_classes([IsAuthenticated])
    @action(detail=False, methods=["post"])
    def followthemes(self, request):
        serializer = UserSerializer()
        serializer.add_user_themes(request.user, request.data)
        return Response(
            {"Exito": "Temas seguidos correctamente"}, status=status.HTTP_200_OK
        )

    @permission_classes([IsAuthenticated])
    @action(detail=False, methods=["get"])
    def logout(self, request):
        request.user.auth_token.delete()
        return Response(
            {"Éxito": "Sesión cerrada correctamente"}, status=status.HTTP_200_OK
        )

    @permission_classes([IsAuthenticated])
    @action(detail=False, methods=["get"])
    def notifications(self, request):
        if not User.objects.filter(username=request.user).exists():
            return Response(
                {"Error": "Requiere sesión activa"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UserNotificacionSerializer(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)
