from django.shortcuts import render
from django.http import HttpResponse

from helloWorld.models import HelloWorld
# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")

