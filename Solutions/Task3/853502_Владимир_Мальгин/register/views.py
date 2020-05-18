from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from .tokens import token_generator
import logging
from email_sender import send

from .models import *
from .forms import *

logger = logging.getLogger(__name__)


class RegisterView(generic.CreateView):
    template_name = 'register/register.html'
    success_template = 'register/success.html'
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user: User = User.objects.create_user(
                form.data.get('username'),
                form.data.get('email'),
                form.data.get('password'))
            new_user.is_active = False
            new_user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('jinja2/acc_activation_email.html', context={
                'user': new_user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token': token_generator.make_token(new_user)
            })
            send(mail_subject, message, [new_user.email])
            logger.info("User registered: " + new_user.username)
            return render(request, self.success_template, context={'email': new_user.email})

        return render(request, self.template_name, {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        logger.info("User activated: " + user.username)
        return render(request, 'register/activation.html',
                      context={'message': 'Thank you for your email confirmation. Now you can login your account.'})
    else:
        return render(request, 'register/activation.html',
                      context={'message': 'Activation link is invalid!'})
