from django.shortcuts import render
from rest_framework import viewsets
from .models.models import Task
from ..serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]

    """ def get_queryset(self):
        return Task.objects.filter(user=self.request.user) """
