from django.test import TestCase
from django.contrib.auth.models import User, Group
from django.test.client import Client as BaseClient, FakePayload

import secretballot
import unittest
from django.http import HttpRequest
from likes.utils import can_vote, likes_enabled


class Client(BaseClient):
    """Bug in django/test/client.py omits wsgi.input"""

    def _base_environ(self, **request):
        result = super(Client, self)._base_environ(**request)
        result['HTTP_USER_AGENT'] = 'Django Unittest'
        result['wsgi.input'] = FakePayload(b'')
        result['Content-Type'] = "text/plain; charset=utf-8"
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
        self.group = Group(name="Test")
        self.group.save()
        self.client = Client()

    def test_like(self):
        # Anonymous vote
        response = self.client.get(
            '/like/auth-user/%s/1' % self.user.id,
            HTTP_REFERER='Dummy'
        )
        # Expect a redirect
        self.assertEqual(response.status_code, 302)

    @unittest.skip("Found bug in django-secretballot with Django 1.8.2+")
    def test_like_ajax(self):
        # Anonymous vote
        response = self.client.get(
            '/like/auth-user/%s/1' % self.user.id,
            HTTP_REFERER='Dummy',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)

    def test_like_bot(self):
        # Anonymous vote from robot (no HTTP_REFERER)
        response = self.client.get(
            '/like/auth-user/%s/1' % self.user.id,
        )
        self.assertEqual(response.status_code, 404)

    def test_like_liked_enabled(self):
        # Test likes_enabled function in utils
        request = HttpRequest()
        self.assertTrue(
            likes_enabled(
                self.user,
                request
            )
        )
        self.assertFalse(
            likes_enabled(
                self.group,
                request
            )
        )

    def test_like_can_vote(self):
        # Test can_vote function in utils
        request = HttpRequest()
        request.secretballot_token = '1.2.3.4'
        self.assertTrue(
            can_vote(
                self.user,
                self.user,
                request
            )
        )
        self.assertFalse(
            can_vote(
                self.group,
                self.user,
                request
            )
        )
