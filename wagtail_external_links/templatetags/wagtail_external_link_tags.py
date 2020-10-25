from urllib.parse import urlparse

from django import template
from django.conf import settings

register = template.Library()


default_domains = [
    settings.BASE_URL,
    "rca-production.herokuapp.com",
    "rca-staging.herokuapp.com",
    "rca-development.herokuapp.com",
    "rca.ac.uk",
    "www.rca.ac.uk",
    "0.0.0.0",
    "localhost",
    "rca-verdant-staging.herokuapp.com",
    "rca-verdant-production.herokuapp.com",
    "beta.rca.ac.uk",
]


@register.simple_tag(name="is_external")
def is_external(*args):
    """
    Work out if a url value or firstof values is in the list of default_domains.
    If it isn't, return True. Instead of populating an href and target together,
    which would be preferable, this is for use when adding suitable targets and
    icons for external links
    example single {% is_external 'https://bbc.co.uk' %} would return True
    example empty {% is_external '' '' %} would return False
    example multiple {% is_external 'https://rca.ac.uk' 'https://bbc.co.uk' %}
    would return False
    Returns:
        Boolean -- True if the url value is not in the list of default domains
    """
    # find the first non empty value
    try:
        link = next(s for s in args if s)
    except StopIteration:
        # incase we get passed empty strings
        return False

    # Catch anchor links
    if link != "#":
        if urlparse(link).hostname not in default_domains:
            return True

    return False
