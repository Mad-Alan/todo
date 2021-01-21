from django.shortcuts import render, HttpResponse
from .models import ToDo

def homepage (request):
    return render(request, "index.html")

def test (request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def first(request):
    return render(request, "index1.html")

def second(request):
    return render(request, "index2.html")

def third(request):
    return render(request, "index3.html")
