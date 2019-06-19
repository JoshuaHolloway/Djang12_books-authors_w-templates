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
def show_book(request, book_id):
  context = specific_book_info(book_id) # To pass into HTML
  return render(request, "books_authors_app/show_book.html", context)
# ======================================================================================================================
def add_book(request):
  if request.method != "POST":
    print("ERROR: Expecting a POST request to be made to this route")
  title = request.POST['title']
  desc = request.POST["desc"]
  book = Book.objects.create(title=title, description=desc)
  context = specific_book_info(book.id) # To pass into HTML
  return render(request, "books_authors_app/show_book.html", context)
# ======================================================================================================================
def assign_author(request, book_id):
  author_id = request.POST['author']

  return redirect("/books/assign_author/" + str(book_id) + "/" + str(author_id))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def assign_author_redirected(request, book_id, author_id):
  book = Book.objects.get(id=book_id)
  author = Author.objects.get(id=author_id)
  book.authors.add(author)
  print("Book-Title: " + str(book.title) + " has authors: " + str(book.authors.all())) # DEBUG

  return redirect("/books/" + str(book_id))
# ======================================================================================================================
def authors(request):
  return render(request, "books_authors_app/authors.html", {"authors": Author.objects.all()})
# ======================================================================================================================
def specific_author_info(author_id):
  # 1. Specific author
  author = Author.objects.get(id=author_id)

  # 2. List of all books this author has written/co-written
  books_authored = author.books.all()

  # 3. All books to be able to select from them in the drop-down
  books = Book.objects.all()

  # To pass into HTML
  return {
    "author": author,
    "books_authored": books_authored,
    "books": books}
# ======================================================================================================================
def show_author(request, author_id):
  context = specific_author_info(author_id) # To pass into html
  return render(request, "books_authors_app/show_author.html", context)
# ======================================================================================================================
def add_author(request):
  if request.method != "POST":
    print("ERROR: Expecting a POST request to be made to this route")
  name = request.POST['name']
  notes = request.POST["notes"]
  author = Author.objects.create(name=name, notes=notes)
  context = specific_author_info(author.id) # To pass into HTML
  return render(request, "books_authors_app/show_author.html", context)
# ======================================================================================================================
def assign_book(request, author_id):
  book_id = request.POST['book']

  return redirect("/author/assign_book/" + str(author_id) + "/" + str(book_id))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def assign_book_redirected(request, author_id, book_id):

  author = Author.objects.get(id=author_id)
  book = Book.objects.get(id=book_id)
  book.authors.add(author)

  # DEBUG
  print("Book-Title: " + str(book.title) + " has authors: " + str(book.authors.all()))

  return redirect("/authors/" + str(author_id))
# ======================================================================================================================
def debug(request, author_id, book_id):
    d = 0
    return 0