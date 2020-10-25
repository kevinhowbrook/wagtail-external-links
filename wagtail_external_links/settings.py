from django.conf import settings

DEFAULTS = {}


class WagtailExternalLinksSettings:
    def __getattr__(self, attr):
        django_settings = getattr(settings, "WAGTAIL_EXTERNAL_LINKS_CONFIG", {})

        try:
            # Check if present in user settings
            return django_settings[attr]
        except KeyError:
            return getattr(DEFAULTS, attr, None)


wagtail_external_links_settings = WagtailExternalLinksSettings()
