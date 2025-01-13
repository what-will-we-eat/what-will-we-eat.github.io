"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
#from django.urls import path, include
from django_distill import distill_path as path
from main import views as main_views


urlpatterns = [
#    path('admin/', admin.site.urls),
    path('', main_views.landing, name='landing'),
    path('program/', main_views.program, name='program'),
    path('team/', main_views.team, name='team'),
    path('news/', main_views.news, name='news'),
    path('output', main_views.output, name='output')
]
