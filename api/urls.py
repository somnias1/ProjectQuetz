from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    UserFollowingViewSet,
    TutorialViewSet,
    TutorialPlumaViewSet,
    PasoViewSet,
    TemaViewSet,
    ComentarioViewSet,
    RespuestaViewSet,
)

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="usuarios")
router.register(r"users/social", UserFollowingViewSet, basename="follows")
router.register(r"tutorials", TutorialViewSet)
router.register(r"tutorials/(?P<tutorial>.+)/steps", PasoViewSet, basename="pasos")
router.register(r"tutorials/feathers", TutorialPlumaViewSet)
router.register(r"themes", TemaViewSet, basename="temas")
router.register(r"comments", ComentarioViewSet, basename="comentarios")
router.register(r"replies", RespuestaViewSet, basename="respuestas")

urlpatterns = [
    path("", include(router.urls)),
]
