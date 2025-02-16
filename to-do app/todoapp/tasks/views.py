from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    tasks = Tasks.objects.all()
    form = TaskForm
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context, )

def updateTask(request, pk):
    task = Tasks.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list')
    form = TaskForm(instance=task)
    
    return render(request, 'tasks/update_tasks.html', {'form': form})
def deleteTask(request, pk):
    item = Tasks.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('list')
    return render(request, 'tasks/delete.html', {'item': item} )