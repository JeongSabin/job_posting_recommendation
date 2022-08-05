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
def db():
    path = '/rec_sys_model/wanted/clear_data/001_웹_data_scaler.csv'
    file = open(path)
    reader = csv.reader(file)
    print('-----', reader)

    list = []

    for row in reader:
        if not bool(post3.objects.filter(Q(page_url=row[1]))):
            list.append(post3(category=row[0],
                              page_url=row[1],
                              picture_url=row[2],
                              title=row[3],
                              company=row[4],
                              work=row[5],
                              qualification=row[6],
                              favor=row[7],
                              welfare=row[8],
                              skill_stack=row[9],
                              place=row[10],
                              money=row[11],
                              employee=row[12],
                              first_cleaned_welfare=row[13],
                              first_cleaned_works=row[14],
                              scaler_money=row[15]))
    post3.objects.bulk_create(list)