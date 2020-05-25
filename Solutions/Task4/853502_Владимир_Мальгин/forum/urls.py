from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("topic/<int:topic_id>", views.topic_details),
    path("theme/<int:theme_id>", views.theme_details),
    path("message/", views.message)
]