# ruff: noqa: E501

from .base import *
from .base import env

# GENERAL
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list(
    "DJANGO_ALLOWED_HOSTS",
    default=["traceu-app.onrender.com", ".onrender.com"]
)

CSRF_TRUSTED_ORIGINS = [
    "https://traceu-app.onrender.com"
]

DEBUG = False

# DATABASE
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)

# CACHE (disable Redis safely)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

# SECURITY (safe defaults for Render)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# STATIC / MEDIA (LOCAL - NO AWS)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# EMAIL (safe fallback)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="Esoft <noreply@example.com>",
)

# ADMIN
ADMIN_URL = env("DJANGO_ADMIN_URL", default="admin/")

# EXTRA APPS
INSTALLED_APPS += [
    "anymail",
]