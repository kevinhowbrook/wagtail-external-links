from django.conf import settings
from django.test import TestCase

from ..settings import wagtail_external_links_settings
from ..templatetags.wagtail_external_link_tags import is_external
from .settings import BASE_URL


class TestExternalLinks(TestCase):
    def test_a_defined_domain(self):
        # If we have defined an internal_domain in the settings,
        # is_external should return False
        self.assertFalse(is_external(BASE_URL))

    def test_nothing_passed(self):
        self.assertFalse(is_external(""))

    def test_an_external_link(self):
        self.assertTrue(is_external("https://github.com"))

    def test_link_orders(self):
        # passing 2 links... return the check for the first found
        self.assertTrue(is_external("https://github.com", BASE_URL))
        self.assertFalse(is_external(BASE_URL, "https://github.com"))
        self.assertFalse(is_external("", BASE_URL))
        self.assertFalse(is_external(BASE_URL, ""))


class TestSettings(TestCase):
    def test_settings(self):
        del settings.WAGTAIL_EXTERNAL_LINKS_CONFIG
        self.assertFalse(wagtail_external_links_settings.internal_domains)
