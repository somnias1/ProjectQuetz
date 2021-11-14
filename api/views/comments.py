from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)

from ..models import Comentario, User, ComentarioComunicado
from ..serializers import (
    ComentarioInfoSerializer,
    ComentarioSerializer,
    ComentarioPlumaSerializer,
    ComentarioComunicadoSerializer,
    ComentarioComunicadoInfoSerializer,
)

from .permissions import IsCommentOwner

from .mixins import GetSerializerClassMixin


class ComentarioViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [IsAuthenticated, IsCommentOwner]
    serializer_action_classes = {
        "list": ComentarioInfoSerializer,
    }

    def get_serializer_context(self):
        context = super(ComentarioViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context


class ComentarioPlumaViewSet(viewsets.GenericViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer()

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
            or not Comentario.objects.filter(id=request.data["comentario"]).exists()
        ):
            return Response(
                {"Error": "Comentario inválido"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = ComentarioPlumaSerializer()
        serializer.add_feather(request.user, request.data)
        return Response(
            {"Exito": "Comentario emplumado correctamente"}, status=status.HTTP_200_OK
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
            or not Comentario.objects.filter(id=request.data["comentario"]).exists()
        ):
            return Response(
                {"Error": "Comentario inválido"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = ComentarioPlumaSerializer()
        serializer.remove_feather(request.user, request.data)
        return Response(
            {"Exito": "Comentario desplumado correctamente"}, status=status.HTTP_200_OK
        )


class ComentarioComunicadoViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = ComentarioComunicado.objects.all()
    serializer_class = ComentarioComunicadoSerializer
    permission_classes = [IsAuthenticated, IsCommentOwner]
    serializer_action_classes = {
        "list": ComentarioComunicadoInfoSerializer,
    }

    def get_serializer_context(self):
        context = super(ComentarioComunicadoViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context
