import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html',{})

def part1(request):
    return render(request,'part1.html',{})

#def part2(request):
#    return render(request,'part2.html',{})
#from bicycle.pythonfile import Stations


def part2(request):
    return render(request,'part2.html',{})

def part3(request):
    return render(request,'part3.html',{})







