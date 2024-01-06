from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def validate_due(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Due date must be in the future.")
        return value


class UserTaskSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["username", "tasks"]