"""
pip install django

создаем джанго проект
django-admin startproject tehnoblog

создаем приложение
./manage.py startapp blog
"""

# регистрируем приложение в intalled_apps (файл settings.py)

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
]


