# Wagtail External Links

[![codecov](https://codecov.io/gh/kevinhowbrook/wagtail-external-links/branch/main/graph/badge.svg?token=Zbmp8IuIQ2)](undefined)

## What is it?

A template tag that checks if a link is internal of external.

## Why?

It's a bit specific, but it's generally bad form to make _all_ external links open in a new tab. So this gives the developers a bit more control on how and where to check for external links. It's also useful to return True or False here so it can be used for url link targets and icons.

## How does it work?

By checking if link values passed in exsist in a list of domains specified as internal only.
Define a list if "internal domains" in settings. These are links that you would always want to be internal, anything not in this list will be counted as external. It also works with `firstof` for mutiple values.

### Example

```
{% is_external 'https://bbc.co.uk' %} would return True
{% is_external '' '' %} would return False (no links)
{% is_external 'https://yoursite.com' 'https://bbc.co.uk' %}   would return False

usage:
{% is_external value.one value.two as is_external %}
<a href="{{ url }}" {% if is_external %}target="_blank"{% endif %}>Some link</a>
```

## Configuration

After installing add to your INSTALLED_APPS

```
INSTALLED_APPS = [
    ...
    'wagtail_external_links',
]
```

Set what domains are going to always be internal by specifying in settings:

```
WAGTAIL_EXTERNAL_LINKS_CONFIG = {
    "internal_domains": [
        'example.com',
        'yoursite.com',
    ]
}
```

To use in a template, first load the template tag by adding the following to your template

```[html]
{% load wagtail_external_link_tags %}

To use:
{% is_external 'https://bbc.co.uk' %}
```
