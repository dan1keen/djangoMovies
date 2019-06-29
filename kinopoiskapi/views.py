from django.shortcuts import render
from django.db import models
from django.views.generic.base import View
from kinopoisk.movie import Movie
import tmdbsimple as tmdb
from tmdbv3api import TMDb
from tmdbv3api import Movie
import requests
import json
from django.shortcuts import render, get_object_or_404
import http.client
# Create your models here.
def getjson(url, data = None):

    response = requests.get(url, params=data)
    print(response.url)
    response = response.json()
    return response
def index(request):
    tmdb3 = TMDb()
    tmdb3.api_key = 'bf4a7e22bb42072d024a9c1b6f88597f'





    movie = Movie()
    popular = movie.popular()
    for p in popular:
        print(p.title)
        print(p.poster_path)
        print("===================BREAKLINE=====================")

    context = {
        'popular': popular
    }
    return render(request, "kinopoiskapi/kinopoisk.html", context)
# Create your views here.

def single_page(request, movie_id):
    conn = http.client.HTTPSConnection("api.themoviedb.org")
    tmdb3 = TMDb()
    tmdb3.api_key = 'bf4a7e22bb42072d024a9c1b6f88597f'
    movie = Movie()
    details = movie.details(movie_id)
    credits = movie.credits(movie_id)


    conn.request("GET", "/3/movie/" + str(movie_id) + "/translations?api_key=" + tmdb3.api_key)
    res = conn.getresponse()
    data = res.read()
    json_data = json.loads(data)
    translations = json_data['translations']
    rus = []
    for indx in range(0,10):
        if translations[indx]['iso_639_1'] == 'ru':
            rus = translations[indx]

    
    context = {
        'details': details,
        'credits': credits,
        "rus": rus,
    }


    return render(request, "kinopoiskapi/single.html", context)