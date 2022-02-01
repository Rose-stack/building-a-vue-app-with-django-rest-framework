from rest_framework import routers,serializers,viewsets
from .models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'created_at']