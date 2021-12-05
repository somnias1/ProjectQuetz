from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    AllowAny,
)
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Comunicado, User
from ..serializers import (
    ComunicadoDetailSerializer,
    ComunicadoSerializer,
    ComunicadoPlumaSerializer,
)

from .permissions import IsAnnounceOwner

from .mixins import GetSerializerClassMixin


class ComunicadoViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    # queryset = Comunicado.objects.all()
    serializer_class = ComunicadoDetailSerializer
    permission_classes = [IsAuthenticated, IsAnnounceOwner]

    serializer_action_classes = {
        "list": ComunicadoSerializer,
    }

    def get_queryset(self):
        user = self.request.user
        following = user.following.values_list("following_user_id", flat=True)
        # comms = Comunicado.objects.filter(comunicador__in=following)
        # print(following, comms)
        queryset = Comunicado.objects.filter(comunicador__in=following).order_by("-id")
        return queryset

    def get_serializer_context(self):
        context = super(ComunicadoViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context


class ComunicadoPlumaViewSet(viewsets.GenericViewSet):
    queryset = Comunicado.objects.all()
    serializer_class = ComunicadoSerializer()

    @permission_classes([IsAuthenticated])
    @action(detail=False, methods=["post"])
    def emplumar(self, request):
        if not User.objects.filter(username=self.request.user).exists():
            return Response(
                {"Error": "Requiere sesión activa"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        if (
            not request.data
            or not Comunicado.objects.filter(id=request.data["comunicado"]).exists()
        ):
            return Response(
                {"Error": "Comunicado inválido"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = ComunicadoPlumaSerializer()
        serializer.add_feather(request.user, request.data)
        return Response(
            {"Exito": "Comunicado emplumado correctamente"}, status=status.HTTP_200_OK
        )

    @permission_classes([IsAuthenticated])
    @action(detail=False, methods=["post"])
    def desplumar(self, request):
        if not User.objects.filter(username=self.request.user).exists():
            return Response(
                {"Error": "Requiere sesión activa"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        if (
            not request.data
            or not Comunicado.objects.filter(id=request.data["comunicado"]).exists()
        ):
            return Response(
                {"Error": "Comunicado inválido"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = ComunicadoPlumaSerializer()
        serializer.remove_feather(request.user, request.data)
        return Response(
            {"Exito": "Comunicado desplumado correctamente"}, status=status.HTTP_200_OK
        )
