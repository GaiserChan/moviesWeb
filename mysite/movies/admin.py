from django.contrib import admin
from .models import Movie
from .models import User
from .models import VideoType
# Register your models here.
admin.site.register(Movie)
admin.site.register(User)
admin.site.register(VideoType)
