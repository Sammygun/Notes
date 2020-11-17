http://127.0.0.1:8000/
http://127.0.0.1:8000/admin

0 python --version смотрю версию если не та установи

 sudo add-apt-repository ppa:deadsnakes/ppa
 sudo apt-get update
 sudo apt-get install python3.8
 python3 # вызов интерпретатора



1 sudo apt install python3-venv
python3 -m venv venv ##создание виртуального окружения
source myvenv/bin/activate

2 python -m pip install Django
pip install django # можно и так 

3 python -m django --version # версия django так можно понять установлен ли вообще django

4 django-admin startproject mysite # создадим проект появится файл manage.py папка mysite/mysite и там все файлы

4.1 нельзя размещать все файлы в корневом каталоге веб-сервера опасно код можжет стать доступным для всех, поэтому код 
надо выносить в отдельную папку (/home/mycode/)
# структура проекта
mysite/ # контейнер нашего проекта
    manage.py # утилита которая позволяет запускать сервер локальный делать миграции баз данных
    mysite/ # это модуль нашего проекта (импорт к примеру mysite.urls)
        __init__.py # пустой файл который сообщает python что каталог это пакет python
        settings.py # конфигурация нашего проекта django
        urls.py # это оглавление нашего проекта, здесь указываю url проекта
        asgi.py # для асихронных приложений 
        wsgi.py # для сихронных приложений

4.2 Пример setings.py
1 DEBUG = True # debug включен на продакшен False

2 ALLOWED_HOSTS = [] # при разработке необязателен, но при деплое на сервере обязательно указать домен

3 INSTALLED_APPS тут все наши приложения подключенные :
админка
аунтефикация
сессии
сообщения
статика и другое

4 middleware # промежуточные слои
5 ROOT_URLCONF = 'django_movie.urls' # указывает на корневые url приложения

6 DATABASES здесь указана как база данных сейчас подключена
sqlite3

7 LANGUAGE_CODE = 'en-us' # язык сайта 'ru' админка станет русской
USE_TZ = True # временная зона

4.3 urls.py #urlconf на чистом python
python  ищет urlpatterns которые прописаны в urls.py типо:

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/<int:year>/', views.year_archive, {'foo': 'bar'}), # третий аргумент должен быть словарь 
]

===========================================
5 manage.py команды
1 python manage.py migrate #создаем базу данных, появится файл db.sqlite3
2 python manage.py startapp movies # создаем новое приложение movies

Изменения в models.py сразу делай миграции:
1  python manage.py makemigrations ###  делаем миграции после внесения изменений в models.py или в setings.py указал новое приложение
2 python manage.py migrate #Добавление в базу данных
2.1 python manage.py sqlmigrate polls 0001 ## 0001_initial.py увижу синтаксис sql !!!!! но по факту ничего не будет

2.2 Повторение 
#Изменение модели (models.py).
python manage.py makemigrations  #для создания миграций этих изменений также это своего рода система контроля версий 
python manage.py migrate # для применения этих изменений в базе данных.

2.3 python manage.py check ## проверка на ошибки в проекте

2.4 python manage.py createsuperuser # создание пользователя админки
3 python manage.py runserver # запускаем сервер по умолчанию работает на порте 8000
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin
Русификация админки в settings.py
LANGUAGE_CODE = 'ru' ## было 'en-us'


4 python manage.py runserver 8080 # по умолчанию сервер работает 
5 python manage.py runserver 0:8000 ## изменение ip так можно

6 python manage.py startapp polls ## создаю новое приложение polls приложение опроса

появится polls/
  __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
===================================================

7 Сразу пишу представление polls/views.py
from django.http import HttpResponse # импотирую httpresponse

def index(request):           # на запрос отдаем текст
    return HttpResponse("Hello, world. You're at the polls index.")


8 создаю в polls/urls.py # создаю urlconf прописываю следующие
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

9 mysite/urls.py корневому urlconf указываю на модуль polls.urls
mysite/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')), # вставляем при помощи include() в список` urlpatterns`
    path('admin/', admin.site.urls),
]
# Функция include() позволяет ссылаться на другие URLconfs(polls/urls.py)

10 http://127.0.0.1:8000/polls/
#Hello, world. You're at the polls index.
 # атрибуты path https://django.fun/docs/django/ru/3.0/intro/tutorial01/

================================================
Tutorial 2 

1 Настройка базы данных
mysite/settings.py
Sqlite # включен по умолчанию для новичка самый раз включен в python
1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
2 однако если хочу использовать другую базу данных то надо пользователя и пароль указывать
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # пример
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
3 Как можно подключить другие базы данных
'django.db.backends.postgresql'
'django.db.backends.mysql'
'django.db.backends.sqlite3'
'django.db.backends.oracle'

4 mysite/settings.py
INSTALLED_APPS
django.contrib.admin - администраторская часть сайта. Вскоре мы будем ее использовать.
django.contrib.auth - система аутентификации.
django.contrib.contenttypes - фреймворк типов данных.
django.contrib.sessions – фреймвор сессий.
django.contrib.messages – фреймворк сообщений.
django.contrib.staticfiles – фреймворк для работы со статическими файлами.
# Что то можно коментировать если оно не нужно в проекте

4.1 #Все эти приложения используют хотя бы одну таблицу базы данных перед migrate
python manage.py migrate # создаем наши базу данных, migrate пробегается по нашиму файлу setings.py и по настройкам создает ее
#Команда migrate запускает миграцию только для приложений в INSTALLED_APPS.


5 polls/models.py # здесь хранится вся информация о базе данных содержит информацию о полях и поведение данных, которые вы храните

from django.db import models


class Question(models.Model): # вопрос и дата публикации
    question_text = models.CharField(max_length=200) # переменная question_text 
    pub_date = models.DateTimeField('date published') # переменная pub_date 


class Choice(models.Model): # текст выбора и подсчета голосов
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # числа
# Каждое поле представлено экземпляром класса Field  
# CharField для символьных полей max_length=200 символов
# DateTimeField для datetime
# IntegerField числовые значения 
# Каждая модель имеет несколько переменных класса, каждая из которых представляет поле базы данных в модели. !!!!!!


6 Сообщаем нашему проекту что установлено приложение polls
mysite/settings.py
INSTALLED_APPS = [
    'polls.apps.PollsConfig', # добавил наше приложение polls в наш проект  
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# 'polls.apps.PollsConfig' потому что polls/apps.py тут указано что PollsConfig, хотя скорее всего бы сработало просто polls,

7 python manage.py makemigrations polls

  polls/migrations/0001_initial.py
    - Create model Question #!!!!
    - Create model Choice #!!!!

polls/migrations/0001_initial.py ## здесь могу что-то руками поправить удобно прежде чем делать migrate

8 python manage.py sqlmigrate polls 0001 ## 0001_initial.py увижу синтаксис sql но по факту ничего не будет

9 python manage.py check ## проверка проекта на ошибок 

10 python manage.py migrate # создаем таблицы моделей в нашей базе данных
#  migrate берет все миграции, которые не были применены и сихронизирует все изменения которые были внесены

11 Знакомство с API
python manage.py shell # вызываем оболочку python
https://django.fun/docs/django/ru/3.0/intro/tutorial02/
# здесь подробно описан пример работы

12 залетаем сюда 
polls/models.py
import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    # ...
    def __str__(self): ## метод str использеутеся для отображения значения на сайте то что идет в шаблон !!!
        return self.question_text

    def was_published_recently(self): ## пользовательский метод к этой модели
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # ...
    def __str__(self): ## ## метод str использеутеся для отображения значения на сайте !!!
        return self.choice_text 
# для отображения объекта на сайте администратора Django и в качестве значения, вставляемого в шаблон при отображении объекта
#https://django.fun/docs/django/ru/3.0/ref/models/instances/#django.db.models.Model.__str__ # другие методы

"""
Обратите внимание на добавление datetime и from django.utils import timezone для ссылки на стандартный модуль Python datetime и утилиты Django,
связанные с часовыми поясами, в django.utils.timezone соответственно
"""
13 #Далее  пример  работы в консоли
#https://django.fun/docs/django/ru/3.0/intro/tutorial02/
==============================
14 Создание пользователя 
python manage.py createsuperuser # пользователь админки
username: admin
Email address: admin@example.com #необязательно
Password: admin
Password (again): admin
Superuser created successfully.

15 python manage.py runserver
http://127.0.0.1:8000/admin

Русификация админки в settings.py
LANGUAGE_CODE = 'ru' ## было 'en-us'


16 Чтобы в админке появилось наше приложение question:
polls/admin.py

from django.contrib import admin

from .models import Question # импортирую с текущей папки models.py !!!!

admin.site.register(Question)

#После чего в админке появится появится POLLS = Questions
=================================================================

Создание первого приложения на Django, часть 3¶