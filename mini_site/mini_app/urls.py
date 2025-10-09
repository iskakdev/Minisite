from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]