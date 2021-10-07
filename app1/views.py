from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

# Create your views here.


def home(request):
    print("home")
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        obj = Task(title=title, description=desc)
        obj.save()

    tasks = Task.objects.all().order_by('-id')
    return render(request, 'home.html', {'tasklist': tasks})


def delete(request, id):
    print("delete")
    task = Task.objects.get(id=id)
    task.delete()
    return home(request)


def update(request, id):
    print("update")
    record = get_object_or_404(Task, pk=id)
    if request.method == "POST":
        record.title = request.POST["title"]
        record.description = request.POST["desc"]
        record.save()
        return redirect("home")

    return render(request, "update.html")
