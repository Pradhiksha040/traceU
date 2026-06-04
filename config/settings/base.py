from pathlib import Path
import environ

# ======================
# PATHS
# ======================
BASE_DIR = Path(__file__).resolve().parent.parent.parent
APPS_DIR = BASE_DIR / "esoft"

# ======================
# ENV
# ======================
env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    env.read_env(str(BASE_DIR / ".env"))

# ======================
# GENERAL
# ======================
DEBUG = env.bool("DJANGO_DEBUG", default=True)

SECRET_KEY = env("DJANGO_SECRET_KEY", default="django-insecure-key")

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

TIME_ZONE = "UTC"
LANGUAGE_CODE = "en-us"

USE_I18N = True
USE_TZ = True

SITE_ID = 1

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ======================
# DATABASE
# ======================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "ATOMIC_REQUESTS": True,
    }
}

# ======================
# URLS
# ======================
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# ======================
# APPS
# ======================
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
]

LOCAL_APPS = [
    "esoft.users",
    "esoft.pages",
    "accounts",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ======================
# MIDDLEWARE
# ======================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # required for django-allauth
    "allauth.account.middleware.AccountMiddleware",
]

# ======================
# TEMPLATES (FIXED)
# ======================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        # ✅ IMPORTANT FIX (your template issue was here)
        "DIRS": [
            BASE_DIR / "esoft" / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ======================
# STATIC / MEDIA
# ======================
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(APPS_DIR / "static")]
STATIC_ROOT = str(BASE_DIR / "staticfiles")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = str(APPS_DIR / "media")

# ======================
# EMAIL
# ======================
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)

EMAIL_HOST = env("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)

EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_TIMEOUT = 5

# ======================
# ADMIN URL (FIXED)
# ======================
ADMIN_URL = env("DJANGO_ADMIN_URL", default="admin/")

# ======================
# AUTH
# ======================
AUTH_USER_MODEL = "users.User"

DJANGO_ADMIN_FORCE_ALLAUTH = env.bool(
    "DJANGO_ADMIN_FORCE_ALLAUTH",
    default=False
)# ======================
# LOGIN SETTINGS
# ======================

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "login"