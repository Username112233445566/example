from django.conf import settings

# Разрешенные хосты (можно оставить пустым для разработки)
ALLOWED_HOSTS = ['*']

# База данных (по умолчанию SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': settings.BASE_DIR / 'db.sqlite3',
    }
}