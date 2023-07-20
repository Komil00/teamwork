from rest_framework import serializers
from teamwork.skills.serializers import SpecialSerializer

from teamwork.tasks.models import STATUS, Tasks
from teamwork.users.api.serializers import EmployerGetSerializer, EmployeeSerializer, TaskListSerializer



class TasksLSerializer(serializers.ModelSerializer):
    employee = TaskListSerializer(read_only=True, many=False)
    # status = StatusSerializer(read_only=True, many=False)
    
    class Meta:
        model = Tasks
        fields = ['id', 'employee', 'title', 'amount', 'time', 'status', 'description']


class TasksRSerializer(serializers.ModelSerializer):
    employee = TaskListSerializer(read_only=True, many=False)
    specialty = SpecialSerializer(read_only=True, many=False)

    class Meta:
        model = Tasks
        fields = ['id', 'employee', 'title', 'amount','created_at', 'time', 'specialty', 'description']
        
class TasksUpdateSerializer(serializers.ModelSerializer):
    employee = TaskListSerializer(read_only=True, many=False)
    specialty = SpecialSerializer(read_only=True, many=False)
    
    class Meta:
        model = Tasks
        fields = ['employee', 'title', 'amount','created_at', 'time', 'specialty', 'description']
        
        
class TasksCreateSerializer(serializers.ModelSerializer):
    # employee = TaskListSerializer(read_only=True, many=False)
    # specialty = SpecialSerializer(read_only=True, many=False)
    
    class Meta:
        model = Tasks
        fields = "__all__"
        