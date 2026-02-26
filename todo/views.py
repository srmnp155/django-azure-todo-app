from django.shortcuts import render, redirect
from .models import Task

def index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect("/")

    tasks = Task.objects.all().order_by("-created")
    return render(request, "todo/index.html", {"tasks": tasks})

def toggle(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = not task.completed
    task.save()
    return redirect("/")

def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("/")
