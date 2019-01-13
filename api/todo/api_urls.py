from django.urls import path, include
from .views import TaskViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet) # Register tasks in 'api/v1' rest framework view

urlpatterns = [
    path('', include(router.urls)),
]
