from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DemonViewSet

router = DefaultRouter()

router.register("Demon", viewset= DemonViewSet)

urlpatterns = [
    path("api/", include(router.urls))
]
