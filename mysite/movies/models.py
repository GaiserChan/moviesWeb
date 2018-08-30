from django.db import models


# Create your models here.

class Movie(models.Model):
    movie_id = models.CharField(max_length=200)
    movie_url = models.CharField(max_length=200)
    movie_points = models.IntegerField(max_length=10)
    movie_begin_time = models.DateTimeField('date published')


class User(models.Model):
    id = models.CharField(max_length=200)
    birth = models.DateTimeField('date published')
    create_time = models.DateTimeField('date published')
    dollar = models.IntegerField(max_length=10)
    icon = models.CharField(max_length=200)
    introduce = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    sex = models.CharField(max_length=5)
    user_name = models.CharField(max_length=100)


class VideoType(models.Model):
    id = models.CharField(max_length=200)
    type_name = models.CharField(max_length=10)
    type_introduce = models.CharField(max_length=100)
