import requests
from allauth.socialaccount.providers.oauth2 import views as oauth2_views
from django.conf import settings
from django.shortcuts import render

from . import provider


class GovBrLoginAdapter(oauth2_views.OAuth2Adapter):
    base_endpoint = "{domain}{path}"
    provider_id = provider.GovBrLoginProvider.id
    access_token_url = base_endpoint.format(
        domain=settings.SOCIALACCOUNT_GOVBR_SSO_DOMAIN,
        path=settings.SOCIALACCOUNT_GOVBR_ACCESS_TOKEN_PATH,
    )
    authorize_url = base_endpoint.format(
        domain=settings.SOCIALACCOUNT_GOVBR_SSO_DOMAIN,
        path=settings.SOCIALACCOUNT_GOVBR_AUTHORIZATION_PATH,
    )
    profile_url = base_endpoint.format(
        domain=settings.SOCIALACCOUNT_GOVBR_SSO_DOMAIN,
        path=settings.SOCIALACCOUNT_GOVBR_USER_INFO_PATH,
    )

    def complete_login(self, request, app, token, response):
        response = requests.get(
            self.profile_url, headers={"Authorization": "Bearer " + str(token)}
        )
        response.raise_for_status()
        extra_data = response.json()
        return self.get_provider().sociallogin_from_response(request, extra_data)


class GovBrLoginView(oauth2_views.OAuth2LoginView):
    def dispatch(self, request, *args, **kwargs):
        provider = self.adapter.get_provider()
        if request.method == "GET":
            return render(
                request,
                "socialaccount/login.html",
                {
                    "provider": provider,
                    "process": request.GET.get("process"),
                },
            )
        return self.login(request, *args, **kwargs)


oauth2_login = GovBrLoginView.adapter_view(GovBrLoginAdapter)
oauth2_callback = oauth2_views.OAuth2CallbackView.adapter_view(GovBrLoginAdapter)
