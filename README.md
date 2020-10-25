# Wagtail External Links

[![codecov](https://codecov.io/gh/kevinhowbrook/wagtail-external-links/branch/main/graph/badge.svg?token=Zbmp8IuIQ2)](undefined)

## What is it?

A template tag that checks if a link is internal of external.

## How does it work?

You can define a list of "internal urls". Urls that you would always wont to be internal, anything not in this list will be counted as external. It also works with `firstof`!

## Why?

It's generally bad form to make _all_ external links open in a new tab. So this gives the developers a bit more control on how and where to check for external links.

## Example:

```
{% is_external 'https://bbc.co.uk' %} would return True
{% is_external '' '' %} would return False (no links)
{% is_external 'https://yoursite.com' 'https://bbc.co.uk' %}   would return False
```
