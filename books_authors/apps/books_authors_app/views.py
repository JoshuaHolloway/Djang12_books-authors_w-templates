from django.shortcuts import render, HttpResponse
from .models import Book, Author
# ======================================================================================================================
# Create your views here.
def index(request):

  context = {"books": Book.objects.all()}

  return render(request, "books_authors_app/index.html", context)
  # return render(request, "books_authors_app/index.html")
# ======================================================================================================================
def show(request, my_val):

  context = {"book": Book.objects.get(id=my_val)}

  # return HttpResponse("books/" + str(my_val))
  return render(request, "books_authors_app/show.html", context)
# ======================================================================================================================
def add(request):
  if request.method == "GET":
    print("a GET request is being made to this route")
  if request.method == "POST":
    print("a POST request is being made to this route")
    title = request.POST['title']
    desc = request.POST["desc"]
    book = Book.objects.create(title=title, description=desc)
    print(Book.objects.all())

  # context = {"book": Book.objects.get(id=my_val)}
  context = {"book": book}


  # return HttpResponse("books/" + str(my_val))
  return render(request, "books_authors_app/show.html", context)
# ======================================================================================================================