# ruff: noqa: E501

from .base import *
from pathlib import Path

# =========================
# GENERAL
# =========================
DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="dev-secret-key",
)

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# =========================
# EMAIL (REAL SMTP MODE)
# =========================
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# 🔴 CHANGE THIS TO YOUR EMAIL
EMAIL_HOST_USER = "yourgmail@gmail.com"

# 🔴 USE GMAIL APP PASSWORD (NOT NORMAL PASSWORD)
EMAIL_HOST_PASSWORD = "your_app_password"

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

EMAIL_TIMEOUT = 10

# =========================
# DEBUG TOOLBAR
# =========================
INSTALLED_APPS += [
    
    "django_extensions",
]

MIDDLEWARE += [
    
]

INTERNAL_IPS = ["127.0.0.1"]

# =========================
# FIX FOR TEMPLATES (IMPORTANT)
# =========================

# Force correct BASE_DIR if base.py is misconfigured
BASE_DIR = Path(__file__).resolve().parent.parent.parent

TEMPLATES[0]["DIRS"] = [
    BASE_DIR / "esoft" / "templates"
]