import requests
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from . import models
from .models import Movie, Genre, Category


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(movies, 10)
    page = request.GET.get('page')
    try:
        per_page = paginator.get_page(page)
    except(EmptyPage, InvalidPage):
        per_page = paginator.page(1)


    records = {
        'movies' : movies,
        'per_page': per_page,
        'genres' : genres,
        'categories': categories,
        'catalog_page': 'active',

    }

    return render(request, "catalog/index.html", records)

class BookDetailView(View):
    def get(self, request, *args, **kwargs):
        movie = get_object_or_404(Movie, pk=kwargs['pk'])
        genres = Genre.objects.all()
        categories = Category.objects.all()
        context = {
            'movie' : movie,
            'genres' : genres,
            'categories':categories,
            'single_page': 'active',
        }
        return render(request, "catalog/single.html", context)
class CatDetailView(View):
    def get(self, request, *args, **kwargs):
        sort_by_cat = get_object_or_404(Category, pk=kwargs['pk'])
        genres = Genre.objects.all()
        categories = Category.objects.all()

        movies = Movie.objects.filter(category_id = sort_by_cat)
        context = {
            'sort_by_cat':sort_by_cat,
            'movies':movies,
            'genres': genres,
            'categories': categories,
            'category_page': 'active',
        }
        return render(request, "catalog/category.html", context)

class GenDetailView(View):
    def get(self, request, *args, **kwargs):
        sort_by_cat = get_object_or_404(Genre, pk=kwargs['pk'])
        genres = Genre.objects.all()
        categories = Category.objects.all()

        movies = Movie.objects.filter(genre = sort_by_cat)
        context = {
            'sort_by_cat':sort_by_cat,
            'movies':movies,
            'genres': genres,
            'categories': categories,
            'genre_page': 'active',
        }
        return render(request, "catalog/genre.html", context)