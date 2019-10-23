# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """Модель статьи"""
    class Meta():
        db_table = "post"
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["create"]

    title = models.CharField("Заголовок", max_length=100)
    text = models.TextField("Текст статьи", max_length=1500)
    image = models.ImageField("Изображение", upload_to="post/", blank=True)
    create = models.DateTimeField("Создан", auto_now_add=True)
    update = models.DateTimeField("Опубликовано", auto_now=True)
    moder = models.BooleanField("Модерация", default=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title



class CommentPost(models.Model):
    """Модель комментариев"""
    class Meta():
        db_table = "comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    text = models.TextField("Текст комментария")
    created = models.DateTimeField("Добавлен", auto_now_add=True)
    moder = models.BooleanField(default=False)
