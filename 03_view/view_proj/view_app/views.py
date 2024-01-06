from rest_framework import viewsets, generics, views
from rest_framework.response import Response
from django_filters import rest_framework as filters

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAPIView(views.APIView):

    def get(self, request):
        task_list = Task.objects.all()
        task_serializer = TaskSerializer(instance=task_list, many=True)
        return Response(task_serializer.data)
    

class TaskFilterViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = "__all__"


class TaskFilter(filters.FilterSet):

    due__gte = filters.DateFilter(field_name="due", lookup_expr="gte")

    class Meta:
        model = Task
        fields = "__all__"


class TaskDueFilterViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TaskFilter