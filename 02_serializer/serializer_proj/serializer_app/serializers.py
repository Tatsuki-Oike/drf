from rest_framework import serializers
from django.utils import timezone
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def validate_due(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Due date must be in the future.")
        return value
    
    # def validate(self, data):
    #     if data.get("due") < timezone.now().date():
    #         raise serializers.ValidationError("Due date must be in the future.")
    #     return data


class TaskSerializerWithUntilDue(serializers.ModelSerializer):
    # 新しいフィールドを追加
    days_until_due = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = "__all__"

    def validate_due(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Due date must be in the future.")
        return value

    def get_days_until_due(self, obj):

        due_date = obj.due
        current_date = timezone.now().date()

        days_until_due = (due_date - current_date).days

        return days_until_due
   
    
class TaxSerializer(serializers.Serializer):

    price = serializers.IntegerField()
    with_tax = serializers.SerializerMethodField()

    def get_with_tax(self, obj):
        return int(obj["price"] * 1.1)
