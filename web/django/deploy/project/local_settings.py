import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "=8)^5ii(5*_nb)rnrb2bfty9^==ypzlz@(+nh9%&i6g^6h*cex"

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

