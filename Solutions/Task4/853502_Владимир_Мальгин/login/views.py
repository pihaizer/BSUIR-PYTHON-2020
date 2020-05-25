from django import views
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
import logging

logger = logging.getLogger(__name__)


class LoginView(views.generic.TemplateView):
    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            logger.info("User logged in: " + user.username)
            return HttpResponse()
        else:
            return HttpResponse("Invalid username or password")
