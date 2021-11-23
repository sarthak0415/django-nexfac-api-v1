from rest_framework import serializers

from .models import User, Asset, Area, Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'date_created', 'task_inputs')

class AssetSerializer(serializers.HyperlinkedModelSerializer):
    tasks = TaskSerializer(read_only=True, many=True)

    class Meta:
        model = Asset
        fields = ('name', 'date_created', 'tasks')

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    tasks = TaskSerializer(read_only=True, many=True)
    
    class Meta:
        model = Area
        fields = ('name', 'date_created', 'tasks')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    areas = AreaSerializer(read_only=True, many=True)
    assets = AssetSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'date_created', 'assets', 'areas')
