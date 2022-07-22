from django.urls import path
from . import views

#URL configuration module

urlpatterns = [
    path('', views.index, name='index'),
    path('part1', views.part1, name='part1'),
    path('part2', views.part2, name='part2'),
    path('part3', views.part3, name='part3')
]