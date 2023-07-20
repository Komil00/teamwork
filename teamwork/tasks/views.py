from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

from rest_framework.response import Response
from rest_framework import status, viewsets

from teamwork.tasks.models import Tasks
from teamwork.tasks.serializers import TasksLSerializer, TasksRSerializer, TasksUpdateSerializer, TasksCreateSerializer


class TasksApiView(ListAPIView):
    queryset = Tasks.objects.filter(is_active=True)
    serializer_class = TasksLSerializer
    
    def get(self, request, *args, **kwargs):
        tasks = self.get_queryset()
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TasksRApiView(RetrieveAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksRSerializer

class TasksUpdateApiView(UpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksUpdateSerializer

class TasksDeleteApiView(DestroyAPIView):
    queryset = Tasks.objects.all()

class TasksCreateApiView(CreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksCreateSerializer