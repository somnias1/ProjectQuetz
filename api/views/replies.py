from rest_framework import status, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import (
    # IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    AllowAny,
)

from ..models import Respuesta
from ..serializers import (
    RespuestaInfoSerializer,
    RespuestaSerializer,
)

from .permissions import IsReplyOwner

from .mixins import GetSerializerClassMixin


class RespuestaViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer
    permission_classes = [IsAuthenticated, IsReplyOwner]
    serializer_action_classes = {
        "list": RespuestaInfoSerializer,
    }

    def get_serializer_context(self):
        context = super(RespuestaViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context
