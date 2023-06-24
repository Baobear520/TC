from .common import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

SECRET_KEY = "django-insecure-bd+4gkm)38!yez%yp&n8necw=(v16t7y65dj97y4s$r26ups42"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "school",
        "USER": "root",
        "PASSWORD":"3010Lbvjy",
    }
}