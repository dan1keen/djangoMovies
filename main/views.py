from django.shortcuts import render

# Create your views here.
from catalog.models import Movie, Genre, Category


def index(request):
    genres = Genre.objects.all()
    categories = Category.objects.all()

    context = {
        'genres': genres,
        'categories': categories,
        'main_page': 'active',
    }
    return render(request, "main/index.html", context)

