from rest_framework import viewsets, views, status
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer, TaskSerializerWithUntilDue, TaxSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUntilDueViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerWithUntilDue


class TaxAPIView(views.APIView):

    def post(self, request):
        tax_serializer = TaxSerializer(data=request.data)
        tax_serializer.is_valid(raise_exception=True)
        return Response(tax_serializer.data)
