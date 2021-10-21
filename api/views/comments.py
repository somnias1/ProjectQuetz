from rest_framework import status, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import (
    # IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    AllowAny,
)

from ..models import Comentario
from ..serializers import (
    ComentarioInfoSerializer,
    ComentarioSerializer,
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
