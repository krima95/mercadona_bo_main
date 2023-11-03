import os
from pathlib import Path
from dj_database_url import parse
from decouple import config

# from storages.backends.s3boto3 import S3Boto3Storage


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
    "drf_spectacular",
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
        "ENGINE": "django.db.backends.postgresql_psycopg2",
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


USE_S3 = os.getenv("USE_S3") == "TRUE"

if USE_S3:
    # AWS settings
    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_SIGNATURE_NAME = config("AWS_S3_SIGNATURE_NAME")
    AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME")
    AWS_S3_FILE_OVERWRITE = config("AWS_S3_FILE_OVERWRITE", cast=bool)
    AWS_DEFAULT_ACL = config("AWS_DEFAULT_ACL")
    AWS_S3_VERITY = config("AWS_S3_VERITY")
    DEFAULT_FILE_STORAGE = config("DEFAULT_FILE_STORAGE")
    STATICFILES_STORAGE = config("STATICFILES_STORAGE")
else:
    STATIC_URL = "/staticfiles/"
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)


# media files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Django session timeout
AUTO_LOGOUT = {
    "IDLE_TIME": 3500,
    "REDIRECT_TO_LOGIN_IMMEDIATELY": True,
    "MESSAGE": "La session est expirée. Veuillez vous reconnecter.",
}  # logout and message

REST_FRAMEWORK = {"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"}

SPECTACULAR_SETTINGS = {
    "TITLE": "Swagger Mercadona API",
}
