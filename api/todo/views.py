from django.shortcuts import render, redirect
from .models import Task
from .serializers import TaskSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    list_tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'list_tasks': list_tasks})

# rest api - DRF    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# rest api - another way
@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        tasks = list(Task.objects.all().values())
        return JsonResponse(tasks, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("Object post successfully!")
            return JsonResponse(serializer.data, status=201)
        else:
            print("Post error:", serializer.errors)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def task_detail(request, id_task):
    """
    Retrieve, update or delete a task
    """
    try:
        task = Task.objects.get(id=id_task)
    except Task.DoesNotExist:
        print("Object not found!")
        return JsonResponse( {"Error": "Object not found!"}, status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            print("Object updated successfully!")
            return JsonResponse(serializer.data, status=204)
        else:
            print("Update error:", serializer.errors)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        if task.delete():
            print("Task ID {} deleted!".format(id_task))
            return HttpResponse(status=204)
