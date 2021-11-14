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
    ComentarioPlumaViewSet,
    RespuestaViewSet,
    ComunicadoViewSet,
    ComunicadoPlumaViewSet,
    ComentarioComunicadoViewSet,
)

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="usuarios")
router.register(r"users/social", UserFollowingViewSet, basename="follows")

router.register(r"tutorials", TutorialViewSet)
router.register(r"tutorials/(?P<tutorial>.+)/steps", PasoViewSet, basename="pasos")
router.register(r"tutorials/feathers", TutorialPlumaViewSet)

router.register(r"themes", TemaViewSet, basename="temas")

router.register(r"comments", ComentarioViewSet, basename="comentarios")
router.register(r"comments/feathers", ComentarioPlumaViewSet)
router.register(r"replies", RespuestaViewSet, basename="respuestas")

router.register(r"announces", ComunicadoViewSet)
router.register(r"announces/feathers", ComunicadoPlumaViewSet)
router.register(r"announcescomments", ComentarioComunicadoViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
