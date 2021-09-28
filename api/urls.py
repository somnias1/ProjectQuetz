from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserFollowingViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="usuarios")
router.register(r"users/social", UserFollowingViewSet, basename="follows")

urlpatterns = [
    path("", include(router.urls)),
]
