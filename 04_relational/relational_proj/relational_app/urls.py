# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserViewSet, UserTaskAPIView

router = DefaultRouter()
router.register('user', UserViewSet)
router.register('task', TaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("user_task/<pk>/", UserTaskAPIView.as_view())
]
