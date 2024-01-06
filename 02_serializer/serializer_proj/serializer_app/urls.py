# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskUntilDueViewSet, TaxAPIView

router = DefaultRouter()
router.register('task', TaskViewSet)
router.register('due', TaskUntilDueViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("tax/", TaxAPIView.as_view()),
]
