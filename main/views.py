from django.shortcuts import render, HttpResponse

def homepage (reguest):
    return HttpResponse("Hala Madrid!")

def test (reguest):
    return render(reguest, "test.html")

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3")
