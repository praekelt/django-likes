import unittest

from django.contrib.auth import get_user_model
from django.test.client import Client as BaseClient, FakePayload
from django.core.handlers.wsgi import WSGIRequest

import secretballot

from likes.templatetags import likes_inclusion_tags
from likes.tests.models import TestModel


class Client(BaseClient):
    """Bug in django/test/client.py omits wsgi.input"""

    def _base_environ(self, **request):
        result = super(Client, self)._base_environ(**request)
        result["HTTP_USER_AGENT"] = "Django Unittest"
        result["HTTP_REFERER"] = "dummy"
        result["wsgi.input"] = FakePayload("")
        return result


class ViewsTestCase(unittest.TestCase):
    """Liking cannot be done programatically since it is tied too closely to a
    request. Do through-the-web tests."""

    @classmethod
    def setUpClass(cls):
        secretballot.enable_voting_on(TestModel)
        cls.client = Client()
        cls.obj1 = TestModel.objects.create()
        cls.obj2 = TestModel.objects.create()

    def test_like(self):
        # Anonymous vote
        response = self.client.get("/like/tests-testmodel/%s/1/" % self.obj1.id)
        # Expect a redirect
        self.assertEqual(response.status_code, 302)

    def test_like_ajax(self):
        # Anonymous vote
        response = self.client.get(
            "/like/tests-testmodel/%s/1/" % self.obj2.id,
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"
        )
        #import pdb;pdb.set_trace()
        self.assertEqual(response.status_code, 200)
