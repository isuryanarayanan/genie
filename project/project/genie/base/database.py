from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.--configuration-key--.sqlite3',
    }
}
