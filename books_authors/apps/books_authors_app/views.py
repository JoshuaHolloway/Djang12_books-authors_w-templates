from django.shortcuts import render, HttpResponse
from .models import Book

# Create your views here.
def index(request):
    # context = {
    #     "name": "Noelle",
    #     "favorite_color": "turquoise",
    #     "pets": ["Bruce", "Fitz", "Georgie"]
    # }
    context = {
    	"books": Book.objects.all()
    }

    return render(request, "books_authors_app/index.html", context)
    # return render(request, "books_authors_app/index.html")

# Create your views here.
def show(request):

    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "books_authors_app/show.html", context)
    # return render(request, "books_authors_app/index.html")