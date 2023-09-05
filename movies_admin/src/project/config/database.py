import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB_NAME'),
        'USER': os.environ.get('POSTGRES_DB_USER'),
        'PASSWORD': os.environ.get('POSTGRES_DB_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('POSTGRES_DB_PORT', 5432),
        'OPTIONS': {'options': '-c search_path=public,content'},
    },
}
