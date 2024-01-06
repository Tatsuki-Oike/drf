from rest_framework import viewsets, views, status
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAPIView(views.APIView):

    def get(self, request):
        task_list = Task.objects.all()
        task_serializer = TaskSerializer(instance=task_list, many=True)
        return Response(task_serializer.data)
    
    def post(self, request):
        task_serializer = TaskSerializer(data=request.data)
        task_serializer.is_valid(raise_exception=True)
        task_serializer.save()
        return Response(task_serializer.data, status.HTTP_201_CREATED)