from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserFollowingViewSet, TutorialViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="usuarios")
router.register(r"users/social", UserFollowingViewSet, basename="follows")
router.register(r"tutorials", TutorialViewSet)
#router.register(r"tutorials/(?P<tutorial>.+)/steps", PasosViewSet,basename="pasos")

urlpatterns = [
    path("", include(router.urls)),
]
