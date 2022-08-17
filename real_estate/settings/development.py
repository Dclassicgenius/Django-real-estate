from .base import *

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "info@estate.com"
DOMAIN = env('DOMAIN')
SITE_NAME = "Estate"

DATABASES = {
    'default': {
      "ENGINE": env("POSTGRES_ENGINE"),  
      "NAME": env("POSTGRES_DB"),
      "USER": env("POSTGRES_USER"),
      "PASSWORD": env("POSTGRES_PASSWORD"),
      "HOST": env("POSTGRES_HOST"),
      "PORT": env("POSTGRES_PORT"), 
      
      }
}