from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import *
from lab3_4.forms import LoginForm


def index(request):
    context = {
        "topics": Topic.objects.order_by("create_date")
    }
    return render(request, "forum/forum.html", context=context)


def topic_details(request, topic_id):
    context = {
        "topic": Topic.objects.get(id=topic_id)
    }
    return render(request, "forum/topic.html", context=context)


def theme_details(request, theme_id):
    context = {
        "theme": Theme.objects.get(id=theme_id),
        "login_form": LoginForm()
    }
    return render(request, "forum/theme.html", context=context)


def message(request, **kwargs):
    print(request.body)
    if request.method == 'POST':
        message_id = request.GET.get('messageId', None)
        theme_id = request.GET.get('themeId', None)
        if not theme_id:
            return HttpResponse(status=400)
        new_message = Message()
        new_message.pub_date = datetime.now()
        new_message.text = request.body.decode('utf-8')
        new_message.sender = request.user
        new_message.theme_id = theme_id
        new_message.save()
        return HttpResponse(status=200)
    elif request.method == 'UPDATE':
        message_id = request.GET.get('messageId', None)
        try:
            msg = Message.objects.get(id=message_id)
        except ObjectDoesNotExist:
            return HttpResponse(status=404)
        msg.text = request.body.decode('utf-8')
        msg.save()
        return HttpResponse(status=200)
    elif request.method == 'DELETE':
        message_id = request.GET.get('messageId', None)
        try:
            msg = Message.objects.get(id=message_id)
        except ObjectDoesNotExist:
            return HttpResponse(status=404)
        msg.delete()
        return HttpResponse(status=200)

