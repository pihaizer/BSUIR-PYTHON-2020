import pytest
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
import register.views
from register.tokens import token_generator


@pytest.mark.django_db
def test_register():
    username = 'new_user_test_123123'
    password = 'test_password_123'
    email = 'noemail@noemail.com'
    request = HttpRequest()
    request.META['HTTP_HOST'] = 'localhost'
    request.POST = {'username': username, 'password': password, 'confirm_password': password, 'email': email}
    view = register.views.RegisterView()
    view.post(request)
    user = User.objects.get(username=username)
    assert user is not None
    assert user.email == email
    assert user.is_active is False
    register.views.activate(HttpRequest(), urlsafe_base64_encode(force_bytes(user.pk)),
                            token_generator._make_token_with_timestamp(user, token_generator._num_days(
                                token_generator._today())))
    user = User.objects.get(username=username)
    assert user.is_active is True
    user.delete()
