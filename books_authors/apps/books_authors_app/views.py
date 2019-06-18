from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author
# ======================================================================================================================
# Create your views here.
def books(request):
  context = {"books": Book.objects.all()}
  return render(request, "books_authors_app/books.html", context)
# ======================================================================================================================
def specific_book_info(book_id):
  # 1. Specific book
  book = Book.objects.get(id=book_id)

  # 2. List of all (co-)authors of this book
  #books_authored = author.books.all() # this is how it is done in show_author()
  co_authors = book.authors.all()

  # 3. All authors (to be able to select from them in the drop-down menu)
  authors = Author.objects.all()

  # To pass into HTML
  return {
    "book": book,
    "co_authors": co_authors,
    "authors": authors}
# ======================================================================================================================
def show_book(request, my_val):
  context = specific_book_info(my_val) # To pass into HTML
  return render(request, "books_authors_app/show_book.html", context)
# ======================================================================================================================
def add_book(request):

  if request.method != "POST":
    print("ERROR: Expecting a POST request to be made to this route")

  title = request.POST['title']
  desc = request.POST["desc"]
  book = Book.objects.create(title=title, description=desc)
  context = specific_book_info(book.id) # To pass into HTML

  # TODO:
  #  1. Pass in co-authors of this specific book
  #  2. Pass in all authors to be able to list them in drop down for addition
  #  Model off of the way that this information is listed in the working SHOW_AUTHOR


  # TODO: After done with this function (above two sub-TODO's) repeat create add_author() function

  return render(request, "books_authors_app/show_book.html", context)
# ======================================================================================================================
def assign_author(request, book_id, author_id):

  book = Book.objects.get(id=book_id)
  author = Author.objects.get(id=author_id)
  book.authors.add(author)

  # DEBUG
  print("Book-Title: " + str(book.title) + " has authors: " + str(book.authors.all()))

  url_to_redirect_to = "books/" + str(book_id)
  print(url_to_redirect_to)

  return redirect("/books/" + str(book_id))
# ======================================================================================================================
def authors(request):
  return render(request, "books_authors_app/authors.html", {"authors": Author.objects.all()})
# ======================================================================================================================
def show_authors(request, my_val):

  # 1. Specific author
  author = Author.objects.get(id=my_val)

  # 2. List of all books this author has written/co-written
  books_authored = author.books.all()

  # 3. All books to be able to select from them in the drop-down
  books = Book.objects.all()

  # To pass into HTML
  context = {
    "author": author,
    "books_authored": books_authored,
    "books": books}

  if request.method == "GET":
    print("a GET request is being made to this route")
  if request.method == "POST":
    print("a POST request is being made to this route")

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
