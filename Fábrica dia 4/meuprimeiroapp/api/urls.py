from rest_framework.routers import DefaultRouter # ver os routers no django rest
from .viewsets import PessoaViewSet, ViaCepViewSet
from django.urls import include, path

router = DefaultRouter()

router.register(prefix="pessoa" , viewset = PessoaViewSet),
router.register("ViaCep", viewset= ViaCepViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
