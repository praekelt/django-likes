import unittest

from likes import middleware, models, urls, views
from likes.templatetags import likes_inclusion_tags


class TestCase(unittest.TestCase):
    def test_something(self):
        1 == 2
        raise NotImplementedError('Test not implemented. Bad developer!')
