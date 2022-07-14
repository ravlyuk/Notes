from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя")
    content = models.TextField(verbose_name="Комментарий")
    published = models.DateTimeField(
        auto_now=True, db_index=True, verbose_name="Опубликовано"
    )
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name="children"
    )
    article = models.ForeignKey(
        Article, # base table
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Статья",
        related_name="comments",
    )

    def __str__(self):
        return self.content[:20] + ".."

    class Meta:
        verbose_name_plural = "Комментарии"
        verbose_name = "Комментарий"
