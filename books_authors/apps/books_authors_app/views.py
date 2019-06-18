from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author
# ======================================================================================================================
# Create your views here.
def books(request):

  context = {"books": Book.objects.all()}

  return render(request, "books_authors_app/books.html", context)
  # return render(request, "books_authors_app/index.html")
# ======================================================================================================================
def show(request, my_val):

  context = {"book": Book.objects.get(id=my_val), "authors": Author.objects.all()}

  if request.method == "GET":
    print("a GET request is being made to this route")
  if request.method == "POST":
    print("a POST request is being made to this route")

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
  context = {"book": book,}

  # return HttpResponse("books/" + str(my_val))
  return render(request, "books_authors_app/show.html", context)
# ======================================================================================================================
def assign_author(request, book_id, author_id):

  book = Book.objects.get(id=book_id)
  author = Author.objects.get(id=author_id)
  book.authors.add(author)

  # DEBUG
  print("Book-Title: " + str(book.title) + " has authors: " + str(book.authors.all()))

  return redirect("/")
# ======================================================================================================================
def authors(request):
  return render(request, "books_authors_app/authors.html", {"authors": Author.objects.all()})
# ======================================================================================================================
def show_authors(request, my_val):

  author = Author.objects.get(id=my_val)
  print(author.name)

  # Grab list of all books this author has written/co-written
  books_authored = author.books.all()

  context = {"author": author, "books_authored": books_authored, "books": Book.objects.all()}
  print(context['author'])




  if request.method == "GET":
    print("a GET request is being made to this route")
  if request.method == "POST":
    print("a POST request is being made to this route")

  # return HttpResponse("books/" + str(my_val))
  return render(request, "books_authors_app/show_author.html", context)
# ======================================================================================================================
def assign_book(request, author_id, book_id):

  print('INSIDE ASSIGN_BOOK()')

  author = Author.objects.get(id=author_id)
  book = Book.objects.get(id=book_id)

  book.authors.add(author)

  # DEBUG
  print("Book-Title: " + str(book.title) + " has authors: " + str(book.authors.all()))

  return redirect("/")
# ======================================================================================================================
