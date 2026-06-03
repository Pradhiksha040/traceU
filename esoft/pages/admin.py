from django.contrib import admin
from django.conf import settings

# SAFE ACCESS (prevents crash)
DJANGO_ADMIN_FORCE_ALLAUTH = getattr(
    settings,
    "DJANGO_ADMIN_FORCE_ALLAUTH",
    False
)

# Optional logic (only runs if True)
if DJANGO_ADMIN_FORCE_ALLAUTH:
    pass

# Register your models here
# (keep empty if you don't have models yet)