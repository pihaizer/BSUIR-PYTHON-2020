"""lab3_4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.news, name='news')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='news')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.news_redirect),
    path("news/", include("news.urls")),
    path("faq/", include("faq.urls")),
    path("forum/", include("forum.urls")),
    path("register/", include("register.urls")),
    path('admin/', admin.site.urls),
    path('login/', include("login.urls")),
    path('logout/', views.logout)
]
