# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskListAPIView, TaskAPIView, TaskFilterViewSet, TaskDueFilterViewSet

router = DefaultRouter()
router.register('task', TaskViewSet)
router.register('filter', TaskFilterViewSet)
router.register('due', TaskDueFilterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("generic/", TaskListAPIView.as_view()),
    path("diy/", TaskAPIView.as_view()),
]
