"""Django settings for CARM Elias project."""

from pathlib import Path

from decouple import Csv, config
from dj_database_url import parse as dburl

BASE_DIR = Path(__file__).resolve().parent.parent

# General
DEBUG = config("DEBUG", cast=bool)
SECRET_KEY = config("SECRET_KEY")
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

TIME_ZONE = "America/Sao_Paulo"
LANGUAGE_CODE = "pt-BR"

SITE_ID = "1"

USE_I18N = True
USE_TZ = True

# Databases
DATABASES = {"default": config("DATABASE_URL", cast=dburl)}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# URLs
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# Apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

if DEBUG:
    INSTALLED_APPS = [
        *INSTALLED_APPS,
        "whitenoise.runserver_nostatic",
        "debug_toolbar",
        "django_extensions",
    ]

INSTALLED_APPS = [
    *INSTALLED_APPS,
    "crispy_forms",
    "crispy_bootstrap5",
]

# Authentication
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]
AUTH_USER_MODEL = "auth.User"
LOGIN_REDIRECT_URL = "users:redirect"
LOGIN_URL = "account_login"

# PASSWORDS
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
]
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE
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
]

if DEBUG:
    MIDDLEWARE = [
        *MIDDLEWARE,
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

# STATIC
STATIC_ROOT = str(BASE_DIR / "staticfiles")
STATIC_URL = "/static/"
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
MEDIA_ROOT = str(BASE_DIR / "media")
MEDIA_URL = "/media/"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# SECURITY
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = "DENY"

# django-debug-toolbar
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": [
        "debug_toolbar.panels.redirects.RedirectsPanel",
        "debug_toolbar.panels.profiling.ProfilingPanel",
    ],
    "SHOW_TEMPLATE_CONTEXT": True,
}
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
