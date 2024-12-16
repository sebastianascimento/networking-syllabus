from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.http import Http404 , HttpResponseNotAllowed
from django.shortcuts import get_object_or_404 , render , redirect
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt


class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Task, pk=pk)

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response({"message": "Tarefa excluída com sucesso"}, status=status.HTTP_204_NO_CONTENT)




def task_list(request):
    tasks = Task.objects.all()  
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = 'completed' in request.POST

        task = Task.objects.create(title=title, description=description, completed=completed)
        return redirect('task_list')  
    return render(request, 'tasks/task_create.html')

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk) 
    return render(request, 'tasks/task_detail.html', {'task': task})



@csrf_exempt
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST" or (request.method == "PUT" and "_method" in request.POST):
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')

    if request.method == "GET":
        return render(request, 'tasks/task_edit.html', {'task': task})

    return HttpResponseNotAllowed(['POST', 'GET'])


@api_view(['DELETE'])
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return Response({"message": "Tarefa excluída com sucesso"}, status=status.HTTP_204_NO_CONTENT)
