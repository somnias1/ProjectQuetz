from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserFollowingViewSet, TutorialViewSet, PasoViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="usuarios")
router.register(r"users/social", UserFollowingViewSet, basename="follows")
router.register(r"tutorials", TutorialViewSet)
router.register(r"tutorials/(?P<tutorial>.+)/steps", PasoViewSet, basename="pasos")

urlpatterns = [
    path("", include(router.urls)),
]
