"""
Unified Django settings for local + production.
"""

import os
import environ
from pathlib import Path
from django.contrib import messages
import dj_database_url

# --------------------------------------------------------------------
# BASE DIR
# --------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR_TEMPLATES = BASE_DIR

# --------------------------------------------------------------------
# ENVIRONMENT
# --------------------------------------------------------------------

env = environ.Env(
    DEBUG=(bool, False),
    ENVIRONMENT=(str, "production")  # "local" or "production"
)

env_path = BASE_DIR / ".env"
if env_path.exists():
    environ.Env.read_env(env_path)

ENVIRONMENT = env("ENVIRONMENT")
DEBUG = env("DEBUG")

# --------------------------------------------------------------------
# SECURITY
# --------------------------------------------------------------------

SECRET_KEY = env("SECRET_KEY")

# Allow all locally, strict in production
ALLOWED_HOSTS = (
    ["*"] if ENVIRONMENT == "local"
    else env.list("ALLOWED_HOSTS", default=["localhost"])
)

CSRF_TRUSTED_ORIGINS = env.list(
    "CSRF_TRUSTED_ORIGINS",
    default=[
        "http://localhost",
        "http://127.0.0.1"
    ] if ENVIRONMENT == "local" else []
)

# In production, HTTPS redirect ON; in local, OFF automatically
SECURE_SSL_REDIRECT = (ENVIRONMENT == "production")

# --------------------------------------------------------------------
# APPLICATIONS
# --------------------------------------------------------------------

INSTALLED_APPS = [
    'home',

    # 3rd party
    'tinymce',
    'rest_framework',
    'watson',
    'corsheaders',
    'crispy_forms',
    'crispy_bootstrap5',
    'captcha',
    'django_bootstrap5',
    'phonenumber_field',
    'cloudinary',
    'cloudinary_storage',

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'corsheaders.middleware.CorsMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR_TEMPLATES / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'portfolio.context_processors.project_context',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'

# --------------------------------------------------------------------
# DATABASE
# --------------------------------------------------------------------

DATABASE_URL = env("DATABASE_URL")
DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}

# --------------------------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --------------------------------------------------------------------
# STATIC / MEDIA / CLOUDINARY
# --------------------------------------------------------------------

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env("CLOUDINARY_CLOUD_NAME"),
    'API_KEY': env("CLOUDINARY_API_KEY"),
    'API_SECRET': env("CLOUDINARY_API_SECRET"),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# --------------------------------------------------------------------
# EMAIL
# --------------------------------------------------------------------

EMAIL_BACKEND = env("EMAIL_BACKEND")
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")

# --------------------------------------------------------------------
# CAPTCHA
# --------------------------------------------------------------------

RECAPTCHA_PUBLIC_KEY = env("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = env("RECAPTCHA_PRIVATE_KEY")
RECAPTCHA_SECRET_KEY = env("RECAPTCHA_PRIVATE_KEY")

# --------------------------------------------------------------------
# ADMIN
# --------------------------------------------------------------------

ADMIN_EMAIL = env("ADMIN_EMAIL")
ADMIN_NAME = env("ADMIN_NAME")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------------------------------------------------------
# TINYMCE
# --------------------------------------------------------------------

TINYMCE_DEFAULT_CONFIG = {
    'height': 500,
    'width': '100%',
    'menubar': True,
    'plugins': (
        'advlist autolink lists link image charmap print preview anchor '
        'searchreplace visualblocks code fullscreen insertdatetime media table '
        'paste code help wordcount autosave emoticons template'
    ),
    'toolbar': (
        'undo redo | formatselect | fontsizeselect | fontselect | '
        'bold italic underline strikethrough forecolor backcolor | '
        'alignleft aligncenter alignright alignjustify | '
        'bullist numlist outdent indent | link image media table | '
        'charmap emoticons | code preview fullscreen | '
        'template insertdatetime | removeformat help'
    ),
    'fontsize_formats': '8pt 10pt 12pt 14pt 18pt 24pt 36pt',
    'font_formats': (
        'Arial=arial,helvetica,sans-serif;'
        'Courier New=courier new,courier,monospace;'
        'Georgia=georgia,palatino;'
        'Tahoma=tahoma,arial,helvetica,sans-serif;'
        'Times New Roman=times new roman,times;'
        'Verdana=verdana,geneva;'
    ),
    'autosave_ask_before_unload': True,
    'autosave_interval': '30s',
    'autosave_retention': '2m',
    'image_advtab': True,
    'content_style': 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }',
}

# --------------------------------------------------------------------
# CRISPY / CORS
# --------------------------------------------------------------------

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# LOCAL mode → allow all origins to avoid CSS/CORS issues
if ENVIRONMENT == "local":
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOW_ALL_ORIGINS = env.bool("CORS_ALLOW_ALL_ORIGINS", default=False)
    CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])

# --------------------------------------------------------------------
# MODE ANNOUNCEMENT
# --------------------------------------------------------------------

print(f"Running in {ENVIRONMENT.upper()} mode")
