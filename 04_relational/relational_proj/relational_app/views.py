from rest_framework import viewsets , generics
from django.contrib.auth.models import User

from .models import Task
from .serializers import TaskSerializer, UserSerializer, UserTaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserTaskAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserTaskSerializer
