from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet

# Criar router para as APIs REST
router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
