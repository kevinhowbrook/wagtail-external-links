from urllib.parse import urlparse

from django import template

from ..settings import wagtail_external_links_settings

register = template.Library()


@register.simple_tag(name="is_external")
def is_external(*args):
    """
    Work out if a url value or firstof values is in the list of default_domains.
    If it isn't, return True. Instead of populating an href and target together,
    which would be preferable, this is for use when adding suitable targets and
    icons for external links
    example single {% is_external 'https://bbc.co.uk' %} would return True
    example empty {% is_external '' '' %} would return False
    example multiple {% is_external 'https://yoursite.com' 'https://bbc.co.uk' %}
    would return False
    Returns:
        Boolean -- True if the url value is not in the list of configured domains
    """
    # find the first non empty value
    try:
        link = next(s for s in args if s)
    except StopIteration:
        # incase we get passed empty strings
        return False

    # Catch anchor links
    # and '/' links that come from page.url values
    return (
        link != "#"
        and link[0] != "/"
        and urlparse(link).hostnme
        not in wagtail_external_links_settings.internal_domains
    )
