from django.shortcuts import render, HttpResponse

def homepage (reguest):
    return HttpResponse("Hala Madrid!")

def test (reguest):
    return render(reguest, "test.html")
