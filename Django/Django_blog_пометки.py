1 
blog/models.py
https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types
Документация типы полей 
Проектируем пост

Post
--------
title # заголовок
text # текст
author # автор
created_date # дата создания
published_date # дата публикации

from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # модель поста, models.Model обрати внимание
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # ForeignKey ссылка на другую модель 
    title = models.CharField(max_length=200) ### тип поля описывается models.Charfield
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): ## метод публикации
        self.published_date = timezone.now()
        self.save()

    def __str__(self): ### после вызова получим строку
        return self.title

====================================
Описание 
class Post(models.Model): — эта строка определяет нашу модель (объект).

class — это специальное ключевое слово для определения объектов.
Post — это имя нашей модели, мы можем поменять его при желании (специальные знаки и пробелы использовать нельзя). Всегда начинай имена классов с прописной буквы.
models.Model означает, что объект Post является моделью Django, так Django поймет, что он должен сохранить его в базу данных.
Дальше мы задаем свойства, о которых уже говорили: title, text, created_date, published_date и author. Чтобы это сделать, нам нужно определиться с типом полей (это текст? число? дата? ссылка на другой объект? например, на пользователя?).

models.CharField — так мы определяем текстовое поле с ограничением на количество символов.
models.TextField — так определяется поле для неограниченно длинного текста. Выглядит подходящим для содержимого поста, верно?
models.DateTimeField — дата и время.
models.ForeignKey — ссылка на другую модель.

2 делаем миграции !!!!
python manage.py makemigrations blog
python manage.py migrate blog



3 Adminka
Чтобы подключить к админке нашу модель POST необходимо сделать следующие
blog/admin.py ## корневая папка проекта не приложение

from django.contrib import admin
from .models import Post ## импортирую нашу модель с классом Post


admin.site.register(Post) # необходимо чтобы наша модель стала доступна в админке

3.1
# http://127.0.0.1:8000/admin
python manage.py createsuperuser # создаем пользователя
admin
admin
Вижу свою модель Post в админке 

3.2 db.sqlite3 локальная база данных проекта находится в самой папке проекта blog(не приложения)
слабая для большого количества пользователей неподходит лучше mysql и postgrel, все посты хранятся в базе данных изменения о них

3.4 Если деллешь репозиторий на github в исключения добавь следующие файлы:
.gitignore
*.pyc
*~
__pycache__
myvenv
db.sqlite3
/static
.DS_Store



URL-адреса Django














26 песня