
from rest_framework import routers,serializers,viewsets
from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at']