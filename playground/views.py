from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    # Pull data from db
    # transform data all these things can be done
    #return HttpResponse("Hello user!")
    return render(request, "edunet.html")

def say_hello_home(request):
    return render(request, "edunet-home.html")

def say_home(request):
    return render(request, "home.html")

def calculator(request):
    return render(request, "calculator.html")

def favorite(request):
    return render(request, "favorite_characters.html")
