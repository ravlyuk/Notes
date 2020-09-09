"""
для отображения моделей в адмнинке
файл admin.py в приложении
"""


from django.contrib import admin

# импорт моделей
from .models import Article, Rubric, Comment


# создание класса для модели
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "name_author",
        "published",
        "rubric",
    )
    # какие поля мы делаем ссылкой на запись
    list_display_links = ("title", "content")
    # какие поля используем для поиска записи
    search_fields = ("title", "content")


# регистрируем модели
admin.site.register(Article, ArticleAdmin)
admin.site.register(Rubric)
admin.site.register(Comment)
