from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def home(request):
    return render(request, 'home.html')

def task_list(request):
    tasks = Task.objects.all()  # Corregido el llamado a "objects"
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Corregido el llamado a "get_object_or_404"
    return render(request, 'task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Definiendo la variable "task"
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()  # Llamada al método "delete" en el objeto "task"
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})