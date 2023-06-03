=====
GovBR Login
=====

GovBR Login is a Django app to connect your system with GovBR social account. With this app,
you can provide a way for users login using GovBR credentials.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "allauth" and "govbr_login" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        # The following apps are required:
        'django.contrib.auth',
        'django.contrib.messages',
        'django.contrib.sites',
        ...
        'allauth',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.openid_connect',
        'govbr_login',
    ]

    SITE_ID = 1

    # Visit https://django-allauth.readthedocs.io/en/latest/installation.html#django for more details

2. Include GovBr domain (staging or production) and paths to login services in your setings like this::

    # GovBR client config
    SOCIALACCOUNT_GOVBR_SSO_DOMAIN = "https://sso.staging.acesso.gov.br"
    SOCIALACCOUNT_GOVBR_AUTHORIZATION_PATH = "/authorize"
    SOCIALACCOUNT_GOVBR_ACCESS_TOKEN_PATH = "/token"
    SOCIALACCOUNT_GOVBR_USER_INFO_PATH = "/userinfo"

    # Visit GovBr tutorial (https://manual-roteiro-integracao-login-unico.servicos.gov.br/pt/stable/iniciarintegracao.html)
    # for more details about required domain and paths

3. Run ``python manage.py migrate`` to create the allauth dependency models.

4. Start the development server and visit http://127.0.0.1:8000/admin/ (you'll need the Admin app enabled) to:

   1. replace 'example.com' site with your url site;
   2. create a SocialApp with GovBr Provider and your url site defined in previous step.

 See tutorial to know how to request client_id and secret_id: https://manual-roteiro-integracao-login-unico.servicos.gov.br/pt/stable/solicitarconfiguracao.html

5. Visit http://127.0.0.1:8000/accounts/govbr/login/ to use your govbr login.