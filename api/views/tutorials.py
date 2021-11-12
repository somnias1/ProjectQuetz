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

from ..models import Tutorial, User
from ..serializers import (
    TutorialDetailSerializer,
    TutorialSerializer,
    TutorialRetrieveSerializer,
    TutorialPlumaSerializer,
)

from .permissions import IsOwnerOrReadOnly

from .mixins import GetSerializerClassMixin


class TutorialViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    serializer_action_classes = {
        "list": TutorialSerializer,
        "retrieve": TutorialRetrieveSerializer,
    }

    search_fields = ["titulo", "descripcion"]
    filter_backends = (
        filters.SearchFilter,
        DjangoFilterBackend,
    )
    filterset_fields = ("nivel", "temas_tutorial")

    def get_serializer_context(self):
        context = super(TutorialViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context


class TutorialPlumaViewSet(viewsets.GenericViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer()

    @permission_classes([IsAuthenticated])
    @action(detail=False, methods=["post"])
    def emplumar(self, request):
        if not User.objects.filter(username=self.request.user).exists():
            return Response(
                {"Error": "Requiere sesión activa"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if (
            not request.data
            or not Tutorial.objects.filter(id=request.data["tutorial"]).exists()
        ):
            return Response(
                {"Error": "Tutorial inválido"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = TutorialPlumaSerializer()
        serializer.add_feather(request.user, request.data)
        return Response(
            {"Exito": "Tutorial emplumado correctamente"}, status=status.HTTP_200_OK
        )

    @permission_classes([IsAuthenticated])
    @action(detail=False, methods=["post"])
    def desplumar(self, request):
        if not User.objects.filter(username=self.request.user).exists():
            return Response(
                {"Error": "Requiere sesión activa"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if (
            not request.data
            or not Tutorial.objects.filter(id=request.data["tutorial"]).exists()
        ):
            return Response(
                {"Error": "Tutorial inválido"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = TutorialPlumaSerializer()
        serializer.remove_feather(request.user, request.data)
        return Response(
            {"Exito": "Tutorial desplumado correctamente"}, status=status.HTTP_200_OK
        )
