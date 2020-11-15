Django 3 создание сайта
https://github.com/Sammygun/Django3
мой gitGitHub


Проект на GitHub - https://github.com/DJWOMS/django_movie

1 Создаю папку Django3 = проваливаюсь:
1 python3  -m venv venv # создаю виртуальное окружение

2 source venv/bin/activate # активирую его в папке Django3
# deactivate # деактивировать
Тоже самое через pycharm только он все сам создаст и настроит виртуальное окружение
просто укажи папку проекта



3 pip install django # устанавлюваю django
4 django-admin startproject django_movie # создание проекта

4.1 python manage.py migrate # появится файл db.sqlite3  создалии базу что и в setings.py прописано

5 python manage.py runserver # запуск сервера
http://127.0.0.1:8000/

5.1  python manage.py startapp movies # создаем новое приложение movies

5.2 python manage.py makemigrations ## теперь делаем миграции после радактирования models.py # это как контроль версий
# если будут ошибки смотри в самом внизу две последние ошибки, самая главная последняя ошибка!!!! 
# SET_NULL!!! папка migration там файл появиться init

5.3 python manage.py migrate ## вот теперь если все успешно реально создали записи в таблице

5.4. после изменений в models.py
1  python manage.py makemigrations ###  делаем миграции
2 python manage.py migrate #Добавление в базу данных
3 в папке migrations появится новый файл c изменениями

5.5. 
python manage.py createsuperuser # создаю пользователя и пароль его
http://127.0.0.1:8000/admin/
user DJWOMS
password DJWOMS
# после этого обязательно перезагрузи локальный сервер!!!!!!


=================
6 В проекте django_movie смотрим рабочие файлы:
ascgi.py # для асихронных приложений
wsgi.py # для сихронных веб-приложений

7 urls.py название доступных страниц




setings.py файл с нашими настройками нашего проекта:
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

8 database создаем базу данных
python manage.py migrate # появится файл db.sqlite3

9 запускаем наш сервер
python manage.py runserver


10 python manage.py startapp movies # создаем новое приложение movies
папка movies файлы:
1 init модуль python
2 admin # все что связано в работе админки
3 apps.py # подключение любой конфигурации
4 models.py будем описывать наши модели таблицы в базе данных
5 tests.py # будем писать тесты
6 views.py # логика нашего веб-приложения html, ошибка 404, перенаправления
7 папка migrations # здесь миграции нашего веб приложения

8 Также в папке movies надо создать forms.py, urls.py пустые

===================================
Уроки Django 3 - создание моделей - урок 4
1 models.py  создание моделей
### Пример кода
from django.db import models # импорт модуля models
from datetime import date

class Category(models.Model): # создаю класс категория
    # Категории
    name = models.Charfield("Категория", max_length=150) # создаю поле с названием CharField это тип
    description = models.TextField("Описание") # поле описание обрати на тип textfield нету ограничений
    url = models.SlugField(max_length=160, unique=True)# поле буквы цифры рамзмер 160 символов 

    def __str__(self): # вернет строку представления нашей модели
        return self.name
    
    class Meta: # контейнер
        verbose_name = "Категория" # имя объекта в единственном числе
        verbose_name_plural = "Категории" # множественное число


class Actor(models.Model): # пишим модель для режисеров и актеров
 # модель актеров и режисеров
    name = models.CharField("Имя", max_length=100) # имя
    age = models.PositiveSmallIntegerField("Возраст", default=0) # возраст по умолчанию 0
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/") # загрузка изображений куда сохранять

   def __str__(self): # вернет строку представления нашей модели
        return self.name
    
    class Meta: # контейнер
        verbose_name = "Актеры и режиссеры" # имя объекта в единственном числе 
        verbose_name_plural = "Актеры и режиссеры" # множественное число

    
class Genre(models.Model):
          #Жанры
    name = models.Charfield("Имя", max_length=100) 
    description = models.TextField("Описание") 
    url = models.SlugField(max_length=160, unique=True) 


    def __str__(self): 
        return self.name
    
    class Meta: 
        verbose_name = "Жанр" 
        verbose_name_plural = "Жанры" 


2 Потом иду в:
setings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'movies',                   # добавлялю наше приложение 
]

3 python manage.py makemigrations ## теперь делаем миграции 
# если будут ошибки смотри в самом внизу две последние ошибки, самая главная последняя ошибка!!!!

3.1 python manage.py migrate    ## вот теперь если все успешно реально создали записи в таблице

======================================================
Уроки Django 3 - таблицы в базе данных и файлы миграций - урок 5
Изменения в models.py сразу делай миграции
1  python manage.py makemigrations ###  делаем миграции
2 python manage.py migrate #Добавление в базу данных
3 в папке migrations появится новый файл c изменениями


========================================================
Уроки Django 3 - создание и вывод фильмов на сайт - урок 6
1 все что вводил в models.py надо импортировать в admin.py
from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews ## все что models.py

admin.site.register(Category) # прописываем таким образом регистрируем нашу модель в админке Django
admin.site.register(Genre)

2 python manage.py createsuperuser # создаю пользователя и пароль его
http://127.0.0.1:8000/admin/
user DJWOMS
password DJWOMS
# после этого обязательно перезагрузи локальный сервер!!!!!!

3 После этого в админке увидим наши модели
2:08