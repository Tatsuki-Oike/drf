import uuid
from django.db import models

class Task(models.Model):

    STATUS_CHOICES = [
        ('todo', 'todo'),
        ('active', 'active'),
        ('done', 'done'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
    due = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)