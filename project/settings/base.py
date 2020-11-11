from pathlib import Path
import os
from chatterbot import comparisons, response_selection

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY", "950xqh!rd9-%7bi_(r8%%vby^%xoy4!jvt%cozr2*t1^x@#fmi"
)

INSTALLED_APPS = [
    "chatterbot.ext.django_chatterbot",
    "gamebot.apps.GamebotConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "project.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Berlin"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Bot settings
CORPUS_DIR = BASE_DIR / "gamebot/corpus/"


CHATTERBOT = {
    "name": "Wolfgang von Beta",
    "logic_adapters": [
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": comparisons.LevenshteinDistance,
            "response_selection_method": response_selection.get_random_response,
        },
    ],
    "trainer": "chatterbot.trainers.ChatterBotCorpusTrainer",
    "training_data": [os.path.join(CORPUS_DIR, "bot.yml")],
}