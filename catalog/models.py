from django.db import models
from django.urls import reverse
# Create your models here.
class Genre(models.Model):
    genre_name = models.CharField(max_length=128)
    def __str__(self):
        return self.genre_name

class Category(models.Model):
    category_name = models.CharField(max_length=56)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name

class Movie(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    genre = models.ManyToManyField(Genre)
    pub_date = models.DateTimeField()
    release_date = models.CharField(max_length=56)
    img = models.ImageField(upload_to="images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=128)

    class Meta:
        ordering = ["-pub_date"]


    def get_absolute_url(self):
        return reverse('model-details', args=[str(self.id)])

    def __str__(self):
        return self.title




