import pytest
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.conf import settings
from importlib import import_module
from login.views import LoginView

test_username = "new_user_test_123123"
test_password = "test_password_123"
test_email = "noemail@noemail.com"


@pytest.fixture
@pytest.mark.django_db
def new_user():
    return User.objects.create_user(username=test_username,
                                    password=test_password,
                                    email=test_email)


@pytest.mark.django_db
@pytest.mark.parametrize(['username', 'password', 'should_login'], [
    (test_username, test_password, True),
    (test_username + '1', test_password, False),
    (test_username, test_password + '1', False)
])
def test_login(username, password, should_login, new_user):
    request = HttpRequest()
    request.META['HTTP_HOST'] = 'localhost'
    engine = import_module(settings.SESSION_ENGINE)
    session_key = None
    request.session = engine.SessionStore(session_key)
    request.POST = {'username': username, 'password': password}
    view = LoginView()
    response = view.post(request)
    if should_login:
        assert response.content == b''
    else:
        assert response.content != b''
    new_user.delete()
