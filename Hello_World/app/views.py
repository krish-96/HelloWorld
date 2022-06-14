from django.shortcuts import render
from django.http import  HttpResponse


# Create your views here.
def home_view(request):
    return HttpResponse("<h2>Welcome to Django World!</h2><h4>This is Hello World Project.</h4><h4>Home Page</h4>")

def index_view(request):
    return render(request, 'index.html')

def other_view(request):
    return render(request, 'others.html')