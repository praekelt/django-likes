from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client as BaseClient, FakePayload
from django.core.handlers.wsgi import WSGIRequest

import secretballot
from likes import middleware, models, urls, views
from likes.templatetags import likes_inclusion_tags


class Client(BaseClient):
    """Bug in django/test/client.py omits wsgi.input"""

    def _base_environ(self, **request):
        result = super(Client, self)._base_environ(**request)
        result['HTTP_USER_AGENT'] = 'Django Unittest'
        result['HTTP_REFERER'] = 'dummy'
        result['wsgi.input'] = FakePayload('')
        return result


class TestCase(TestCase):
    """Liking cannot be done programatically since it is tied too closely to a
    request. Do through-the-web tests."""

    def setUp(self):
        secretballot.enable_voting_on(User)
        self.user = User.objects.create_user(
            'john',
            'john@foo.com',
            'password'
        )
        self.client = Client()

    def test_like(self):
        # Anonymous vote
        response = self.client.get('/like/auth-user/%s/1' % self.user.id)
        # Expect a redirect
        self.assertEqual(response.status_code, 302)

    def test_like_ajax(self):
        # Anonymous vote
        response = self.client.get(
            '/like/auth-user/%s/1' % self.user.id,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
