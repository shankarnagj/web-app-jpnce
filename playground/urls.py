from django.urls import path
from . import views

#URL configuration
urlpatterns =[
    path('hello/', views.say_hello),
    path('hello/home/', views.say_hello_home),
    path('', views.say_home),
    path('calculator/', views.calculator),
    path('favorite/', views.favorite),
]