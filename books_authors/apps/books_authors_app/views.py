from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "books_authors_app/index.html")
    # return HttpResponse("this is the equivalent of @app.route('/')!")