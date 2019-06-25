from django.contrib import admin
from catalog.models import Movie
from catalog.models import Genre
from catalog.models import Category

# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Category)
