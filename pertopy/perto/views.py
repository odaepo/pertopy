from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task, Status


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})



def create_task(request):
    current_status = Status.objects.get(title="incorso")  # Sostituisci con il metodo appropriato per ottenere lo stato corrente

    if request.method == 'POST':
        form = TaskForm(current_status, request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')  # Sostituisci con il nome dell'URL appropriato
    form = TaskForm(current_status)
    return render(request, 'create_task.html', {'form': form})

    return render(request, 'create_task.html',{})
def createAuto_task(request):
    current_status = Status.objects.get(title="incorso")  # Sostituisci con il metodo appropriato per ottenere lo stato corrente

    if request.method == 'POST':
        form = TaskForm(current_status, request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')  # Sostituisci con il nome dell'URL appropriato

    form = TaskForm(current_status)
    return render(request, 'create_task.html', {'form': form})


