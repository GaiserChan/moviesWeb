import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Movie(models.Model):
    movie_id = models.CharField(max_length=200)
    movie_url = models.CharField(max_length=200)
    movie_points = models.IntegerField()
    movie_begin_time = models.DateTimeField('date published')

    def __str__(self):
        return self.movie_id

    def was_published_recently(self):
        return self.movie_begin_time >= timezone.now() - \
               datetime.timedelta(days=1)


class User(models.Model):
    user_id = models.CharField(max_length=200)
    birth = models.DateTimeField('date published')
    create_time = models.DateTimeField('date published')
    dollar = models.IntegerField()
    icon = models.CharField(max_length=200)
    introduce = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    sex = models.CharField(max_length=5)
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name


class VideoType(models.Model):
    video_id = models.CharField(max_length=200)
    type_name = models.CharField(max_length=10)
    type_introduce = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name
