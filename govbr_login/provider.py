from allauth.socialaccount import providers
from allauth.socialaccount.providers.openid_connect.provider import (
    OpenIDConnectProvider,
)
from django.conf import settings


class GovBrLoginProvider(OpenIDConnectProvider):
    id = "govbr_login_openid_connect"
    slug = "govbr"
    name = "GovBR Login (OpenID Connect)"
    scopes = ("openid", "email", "phone", "profile")
    KC_IDP_HINT_PARAM = "kc_idp_hint"

    @property
    def server_url(self):
        return settings.SOCIALACCOUNT_GOVBR_SSO_DOMAIN

    def extract_common_fields(self, data):
        commom_fields = super().extract_common_fields(data)
        commom_fields["phone_number"] = data.get("phone_number")
        return commom_fields

    def get_default_scope(self):
        return self.scopes
    
    def get_login_url(self, request, **kwargs):
        hint_value = settings.SOCIALACCOUNT_GOVBR_KC_IDP_HINT
        if hint_value:
            kwargs[self.KC_IDP_HINT_PARAM] = hint_value
        return super().get_login_url(request, **kwargs)


# https://django-allauth.readthedocs.io/en/latest/advanced.html#customizing-providers
provider_classes = [GovBrLoginProvider]
providers.registry.register(GovBrLoginProvider)
