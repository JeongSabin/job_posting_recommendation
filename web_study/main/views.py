from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *
import csv
from django.db.models import Q

# index.html 페이지를 부르는 index 함수
def index(request):

    return render(request, 'main/index.html')

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    postlist = post3.objects.all()

    return render(request, 'main/blog.html', {'postlist':postlist})

def Post(request):

    return render(request, 'main/index.html')