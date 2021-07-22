from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.


def index(request):

    #получить все объекты из модели
    #tasks = Task.objects.all()

    #sort by
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта',
                                               'tasks': tasks})

def about(request):
    return render(request, "main/about.html")

def create(request):
    error = ''
    if  request.method == "POST":
        form = TaskForm(request.POST)

        #check to error
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма не верна'

    form = TaskForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, "main/create.html", context)