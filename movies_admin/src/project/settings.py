import os
from pathlib import Path

from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()

include(
    "config/paths.py",
    "config/database.py",
    "config/apps.py",
    "config/middleware.py",
    "config/security.py",
    "config/templates.py",
    "config/internationalization.py",
)

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.environ.get("DEBUG", False) == "True"

ROOT_URLCONF = "project.urls"

WSGI_APPLICATION = "project.wsgi.application"

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
