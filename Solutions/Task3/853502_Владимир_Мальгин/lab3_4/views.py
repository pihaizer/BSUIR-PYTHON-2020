from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django import forms


def news_redirect(request):
    return HttpResponsePermanentRedirect("news")


def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    redirect = HttpResponseRedirect(request.META['HTTP_REFERER'])
    return redirect
