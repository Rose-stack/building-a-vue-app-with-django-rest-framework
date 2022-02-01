from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import TodoSerializer
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def todos(request):

    '''
    List all todo snippets
    '''
    if(request.method == 'GET'):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return JsonResponse(serializer.data,safe=False)

    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def todo_detail(request,pk):

    try:
        todo = Todo.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if(request.method == 'PUT'):
        data = JSONParser().parse(request)
        serializer = TodoSerializer(todo,data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif(request.method == 'DELETE'):
        todo.delete()
        return HttpResponse(status=204)
