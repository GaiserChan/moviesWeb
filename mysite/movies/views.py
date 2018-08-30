from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('Hello,movies. You`re at the movie index.')
