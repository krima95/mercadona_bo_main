import os
from pathlib import Path
import dj_database_url
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("MER_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("MER_DEBUG", cast=bool)

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "products",
    "defender",
    "crispy_forms",
    "rest_framework",
    "dj_database_url",
    "whitenoise.runserver_nostatic",
    "storages",
    "django.contrib.sites",
    "cms",
    "menus",
    "treebeard",
    "django_check_seo",
]

SITE_ID = 1

CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "defender.middleware.FailedLoginMiddleware",
    # "django.contrib.staticfiles.middleware.StaticFilesMiddleware",
    "django_auto_logout.middleware.auto_logout",  # django auto logout
]

ROOT_URLCONF = "mercadona.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
                "django_auto_logout.context_processors.auto_logout_client",  # django auto logout
            ],
        },
    },
]

WSGI_APPLICATION = "mercadona.wsgi.application"

# Render postgresQL Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
"""
# Session engine
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Session cookie age (par exemple, 1209600 seconds = 2 semaines)
SESSION_COOKIE_AGE = 1209600

SESSION_COOKIE_SECURE = True
"""

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "fr-FR"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# URL de base pour servir des fichiers depuis MEDIA_ROOT
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

AWS_ACCESS_KEY_ID = "AKIAZT4LFXT2YBXSXBUH"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "mercadonabo"
AWS_S3_SIGNATURE_NAME = "s3v4"
AWS_S3_REGION_NAME = "us-east-1"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# Django session timeout
AUTO_LOGOUT = {
    "IDLE_TIME": 3500,
    "REDIRECT_TO_LOGIN_IMMEDIATELY": True,
    "MESSAGE": "La session est expirée. Veuillez vous reconnecter.",
}  # logout and message
