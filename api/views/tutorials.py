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

from ..models import Tutorial
from ..serializers import (
    TutorialDetailSerializer,
    TutorialSerializer,
    TutorialRetrieveSerializer,
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
