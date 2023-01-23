from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet


router = routers.DefaultRouter()
router.register(r'todo', TaskViewSet)

print(router.urls)

urlpatterns = [
    path('', include(router.urls))
]
