from django.contrib import admin
from django.urls import path
from TrinityCoreApp import views


urlpatterns = [
    path('',views.home,name='TrinityCoreApp'),
    path('about',views.about,name='TrinityCoreApp'),
    path('version',views.version,name='TrinityCoreApp'),
    path('static\sample.txt',views.text,name='TrinityCoreApp'),
    path('submitquery',views.submitquery,name='submitquery')
]