from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def index(request):
    context = {
        "faq": QA.objects.all()
    }
    return render(request, "faq/faq.html", context=context)
