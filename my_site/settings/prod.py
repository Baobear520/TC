import os
from .common import *



DEBUG = False

ALLOWED_HOSTS = []

SECRET_KEY = os.environ['SECRET_KEY']

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True



