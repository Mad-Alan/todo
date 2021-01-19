from django.shortcuts import render, HttpResponse

def homepage (request):
    return render(request, "index.html")

def test (request):
    return render(request, "test.html")

def first(request):
    return render(request, "index1.html")

def second(request):
    return render(request, "index2.html")

def third(request):
    return render(request, "index3.html")
