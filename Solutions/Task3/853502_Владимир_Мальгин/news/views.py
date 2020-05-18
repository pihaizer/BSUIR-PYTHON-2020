from django.shortcuts import render

from .models import *
from lab3_4.forms import LoginForm


def index(request):
    context = {
        'news': get_latest_news(),
        'login_form': LoginForm()
    }
    return render(request, "news/news.html", context=context)


def get_latest_news():
    return Post.objects.order_by("-pub_date")[:3]

