from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from ..serializers import TemaSerializer
from ..models import Tema
#from .permissions import IsAdminUserOrReadOnly

class TemaViewSet(viewsets.ModelViewSet):
    serializer_class = TemaSerializer
    permission_classes = (
        DjangoModelPermissionsOrAnonReadOnly,
    )
    queryset = Tema.objects.all()