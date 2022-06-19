"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from MyApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/',views.sam,name='sample'),
    path('hello/',views.hello,name='hlo'),
    path('style/',views.style,name='st'),


    path('dynamic/<int:id>/',views.dyn,name='dynamic'),
    path('home/<str:name>/',views.home,name='home'),
    path('task/<str:name>/<int:id>/',views.task,name='task'),


    path('temp/',views.temp,name='temp'),
    path('table/',views.table,name='table'),
    path('register/',views.register,name='register'),
    path('data/<str:name>/<int:id>/',views.data,name='data'),


    path('inline/',views.inline,name='inline'),
    path('internal/',views.internal,name='internal'),
    path('external/',views.external,name='external')

]
