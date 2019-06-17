from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "books_authors_app/index.html", context)
    # return render(request, "books_authors_app/index.html")
    # return HttpResponse("this is the equivalent of @app.route('/')!")