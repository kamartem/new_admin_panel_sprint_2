import os
from pathlib import Path

PROJECT_PATH_NAME = Path(__file__).parent.name
DJANGO_ROOT = Path(__file__).parent.parent
PROJECT_ROOT = Path(__file__).parent.parent.parent
LOCALE_PATHS = [os.path.join(os.path.join(DJANGO_ROOT, PROJECT_PATH_NAME), 'locale')]
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATICFILES_DIRS = [DJANGO_ROOT / PROJECT_PATH_NAME / 'static']
