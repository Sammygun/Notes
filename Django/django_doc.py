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

7 LANGUAGE_CODE = 'en-us' # язык сайта
USE_TZ = True # временная зона

4.3 urls.py #urlconf на чистом python
python  ищет urlpatterns которые прописаны в urls.py типо:

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/<int:year>/', views.year_archive, {'foo': 'bar'}), # третий аргумент должен быть словарь 
]

5 manage.py команды
1 python manage.py migrate #создаем базу данных, появится файл db.sqlite3
2 python manage.py startapp movies # создаем новое приложение movies

Изменения в models.py сразу делай миграции:
1  python manage.py makemigrations ###  делаем миграции
2 python manage.py migrate #Добавление в базу данных


3 python manage.py runserver # запускаем сервер по умолчанию работает на порте 8000
http://127.0.0.1:8000/

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