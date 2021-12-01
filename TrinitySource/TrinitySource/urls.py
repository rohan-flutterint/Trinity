"""TrinitySource URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

admin.site.site_header="TRINITY ADMIN"
admin.site.site_title = "TRINITY Admin Portal"
admin.site.index_title = "WELCOME TO TRINITY PRICE CALCULATOR PORTAL"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('TrinityCoreApp.urls')),
    path('about',include('TrinityCoreApp.urls')),
    path('version',include('TrinityCoreApp.urls')),
    path('text',include('TrinityCoreApp.urls'))
]
