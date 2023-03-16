from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TaskForm
from .models import Task, Status


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

class TaskUpdateView(UpdateView):
    model = Task
    #form_class = TaskForm
    fields = ['title', 'description', 'status', 'min', 'max', 'attuale', 'priorita', 'impotanza', 'minuti', 'contesto', 'scadenza']
    #template_name_suffix = '_update_form'
    template_name = 'update_task.html'

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


