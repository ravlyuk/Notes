# pip install psycopg2-binary

# in settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tehnoblog_db',
        'USER': 'yerav',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}