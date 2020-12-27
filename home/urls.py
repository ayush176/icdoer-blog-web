from django.contrib import admin
from django.urls import path ,include
from home import views
urlpatterns = [
    path('',views.home ,name='home'),
    path('contact',views.contact ,name='contact'),
    path('about',views.about ,name='about'),
    path('search',views.search ,name='query'),
    path('signup',views.handleSignup ,name='hanleSignup'),
    path('login',views.handleLogin ,name='hanleLogin'),
    path('logout',views.handleLogout ,name='hanleLogout'),
]