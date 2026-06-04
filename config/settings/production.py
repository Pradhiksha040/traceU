# ruff: noqa: E501

from .base import *  # noqa
from .base import env

# GENERAL
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["example.com"])

# DATABASE
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)

# CACHE (Redis)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

# SECURITY
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# AWS STORAGE
AWS_ACCESS_KEY_ID = env("DJANGO_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("DJANGO_AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("DJANGO_AWS_STORAGE_BUCKET_NAME")

AWS_QUERYSTRING_AUTH = False

_AWS_EXPIRY = 60 * 60 * 24 * 7

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": f"max-age={_AWS_EXPIRY}",
}

AWS_S3_REGION_NAME = env("DJANGO_AWS_S3_REGION_NAME", default=None)
AWS_S3_CUSTOM_DOMAIN = env("DJANGO_AWS_S3_CUSTOM_DOMAIN", default=None)

aws_s3_domain = (
    AWS_S3_CUSTOM_DOMAIN
    or f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
)

MEDIA_URL = f"https://{aws_s3_domain}/media/"
STATIC_URL = f"https://{aws_s3_domain}/static/"

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {"location": "media"},
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {"location": "static"},
    },
}

# EMAIL (MAILGUN / ANYMAIL)
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"

ANYMAIL = {
    "MAILGUN_API_KEY": env("MAILGUN_API_KEY"),
    "MAILGUN_SENDER_DOMAIN": env("MAILGUN_DOMAIN"),
    "MAILGUN_API_URL": env(
        "MAILGUN_API_URL",
        default="https://api.mailgun.net/v3"
    ),
}

DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="Esoft <noreply@example.com>",
)

SERVER_EMAIL = DEFAULT_FROM_EMAIL

EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="[Esoft] ",
)

ACCOUNT_EMAIL_SUBJECT_PREFIX = EMAIL_SUBJECT_PREFIX

# ADMIN
ADMIN_URL = env("DJANGO_ADMIN_URL")

# EXTRA APPS
INSTALLED_APPS += [
    "anymail",
    "collectfasta",
]