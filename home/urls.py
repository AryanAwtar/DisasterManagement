from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('signup', views.signup, name='signup'),
    path('login', views.Login, name='login'),
    path('next', views.next, name='next'),

]