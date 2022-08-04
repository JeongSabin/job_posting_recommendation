from django.urls import path, include

from . import views

app_name = 'rec_job'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register),
]