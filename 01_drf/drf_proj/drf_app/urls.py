# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskAPIView

router = DefaultRouter()
router.register('task', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("diy/", TaskAPIView.as_view())
]
