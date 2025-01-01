from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)  # поле даты публикации
    created = models.DateTimeField(auto_now_add=True)  # поле даты создания
    updated = models.DateTimeField(auto_now=True)  # поле даты изменения

    def __str__(self):
        return self.title
