from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return HttpResponse("This is myapp/Courses page. ")
def about(request):
    return HttpResponse("This is myapp/about page. ")
def myapp(request):
    return HttpResponse("This is myapp page. ")