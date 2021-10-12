from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    AllowAny,
)

from django.http import Http404

from ..models import Paso
from ..serializers import PasoSerializer

from .permissions import IsTutorialOwner


class PasoViewSet(viewsets.ModelViewSet):
    serializer_class = PasoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsTutorialOwner]

    def get_serializer_context(self):
        context = super(PasoViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context

    def get_queryset(self):
        qs = Paso.objects.filter(tutorial_padre__id=self.kwargs["tutorial"])
        return qs

    def get_object(self):
        obj = self.get_queryset().filter(numero_paso=self.kwargs["pk"]).first()
        if obj:
            return obj
        raise Http404
