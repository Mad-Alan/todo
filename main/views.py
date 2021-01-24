from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import library

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

def books_def(request):
    books_list = library.objects.all()
    return render(request, "books.html", {"books_list": books_list})

def add_todo(request):
    form = request.POST
    text = form ["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo (request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo (request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = not todo.is_favorite
    todo.save()
    return redirect(test)

def add_book(request):
    form = request.POST
    book = library (
        title = form["book_title"],
        subtitle = form["book_subtitle"],
        description = form["book_description"],
        price = form["book_price"],
        genre = form["book_genre"],
        author = form["book_author"],
        year = form["book_year"][:10],
    )
    book.save()
    return redirect(books_def)

def delete_book (request, id):
    book = library.objects.get(id=id)
    book.delete()
    return redirect(books_def)

def mark_book (request, id):
    book = library.objects.get(id=id)
    book.is_favorite = not book.is_favorite
    book.save()
    return redirect(books_def)

def BooksDetail (request, id):
    book_object = library.objects.get(id=id)
    return render(request, "books_detail.html",{"book_object": book_object})

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)