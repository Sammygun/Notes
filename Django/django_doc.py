http://127.0.0.1:8000/
http://127.0.0.1:8000/admin

pip install -r requirements.txt  ### когда скачиваю с github устанавливаю все зависимости из этого файла

=================================
Установка django2 
1 mkdir djangogirls
2 cd djangogirls
3 python3 -m venv myvenv # создание вирутального окружения
4 source myvenv/bin/activate # активация
5 python3 -m pip install --upgrade pip ## установка последней версии pip
6 djangogirls/requirements.txt # создал файл там указал данную запись
Django~=2.2.4
7 pip install -r requirements.txt
=================================
Создаю настраиваю django3 
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
==================================


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
#python manage.py makemigrations blog # название приложения в конце возможно надо дописывать 
# python manage.py migrate blog # название приложения

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

6.1 python manage.py test polls ## запускаем тесты из файла tests.py приложения polls(polls/tests.py) 

7 from . import views ## подключил views.py который в текущей папке  лежит
8 polls/views.py ## если мы создали страницу html в polls/templates/polls то здесь должны сделать ее представление
9 polls/url.py ### URLconf 


10 
def get_queryset(self):
    """Возвращает 5 последних опубликованных вопросо"""
    return Question.objects.order_by('-pub_date')[:5]          #!!!!!!!!!! пример использования


11 
СТАТИКА пример статики
1 polls/templates/ # это где хранится html страницы
2 polls/static/polls ### где хранится статика помни надо указывать setings.py
polls/static/polls/style.css. ## как пример
3 polls/style.css ## ссылаться наа этот статический файл в Django можно так


1 polls/static/polls/style.css¶ # пример статики
li a {
    color: green;
}


2 Пример подключение стилей в наш html
polls/templates/polls/index.html
{% load static %} # это тег  генерирует абсолютный URL-адрес статических файлов

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}"> 
# обрати внимание как подключение преоисходит polls/style.css (без полного пути polls/static/polls/style.css!!!!)

3 После чего по следующей ссылке отобразится зеленый цвет
http://127.0.0.1:8000/polls/ ### по ссылке /polls/ # приложение polls

4 Добавление изображения пример
1 polls/static/polls/images ## сюда закидываю картинку 

2 polls/static/polls/style.css¶
body {
    background: white url("images/моя_картинка.gif") no-repeat; #background картинка
}


5  Настройка шаблонов вашего проекта в setings.py
 mysite/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], #### вот эту строку надо добавить обязательно хорошая практика!!!!!!!!!
        'APP_DIRS': True, ## если не сделать то что выше то django просто будет искать по умолчанию подкаталог templates
#DIRS - список каталогов файловой системы, которые нужно проверить при загрузке шаблонов Django; это путь поиска.

5.1 python -c "import django; print(django.__path__)" # узнать где находится  исходные файлы в Django в вашей системе



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
1 views.py # предтсавление здесь описан какой тип страницы будет использоваться в нашем приложении

polls/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
# %s." % question_id когда клиент вводит /polls/34/ будет вывожится текст выше номер 34
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

2 polls/urls.py ### сразу же подключаем описанные выше представления

from django.urls import path

from . import views ## подключил views.py который в текущей папке 

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

3 Теперь смотри /polls/34/ сработает метод detail() описаннный в views.py отобразит любое число которое будет вводить пользователь
Также «/polls/34/results/» и «/polls/34/vote/» - они отобразят результаты и страницы голосования.

Обрати внимание 
pols.views.py 
def vote(request, question_id): ## функци vote и ее атрибуты
    return HttpResponse("You're voting on question %s." % question_id)


polls/urls.py
path('<int:question_id>/vote/', views.vote, name='vote'),
 
4 polls/views.py # добавил

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

5 polls/templates/polls ## создаю папки
# в каждом приложении django ищет папку templates в кажлом installed apps(setings.py)
index.html

{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}

5 polls/views.py ## бежим в views.py если создали страницу в templates/polls/index.html делаем ее представление

from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] # здесь переменнная
    context = {'latest_question_list': latest_question_list} ### словарь с ключом и значением 
    return render(request, 'polls/index.html', context) ###

#Функция render() принимает объект запроса в качестве первого аргумента, имя шаблона в качестве 
#второго аргумента и словарь в качестве необязательного третьего аргумента. Она возвращает объект HttpResponse данного шаблона, отображенный в данном контексте.
==================

Ошибка 404 

1 делаем исключение 
polls/views.py

from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id) ## если введем это
    except Question.DoesNotExist: ## исключение тогда выводим следующую страницу 
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question}) ### возвращаем следующие надо создавать detail.html

2 polls/templates/polls/detail.html¶
{{ question }} ## создаю страницу detail.html и ввожу следующие

3 404 ошибка если объект не существует то вызываем функцию get()
polls/views.py¶
from django.shortcuts import get_object_or_404, render

from .models import Question


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

Функция get_object_or_404() принимает модель Django в качестве первого аргумента и произвольное количество ключевых аргументов,
 которое она передает в get() - функцию менеджера модели. Он вызывает Http404, если объект не существует.

Также есть функция get_list_or_404(), которая работает так же, как get_object_or_404() - за исключением использования filter() 
вместо get(). Он вызывает Http404, если список пуст.


4 polls/templates/polls/detail.html¶
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>



5 Добавляю app_name  

polls/urls.py¶
from django.urls import path

from . import views

app_name = 'polls' ## для того чтобы django отличать разные urls для разных приложений
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


5.1 Теперь мы указываем пространство имен
polls/templates/polls/index.html
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>



==============================================================================

Создание первого приложения на Django, часть 4

1 polls/templates/polls/detail.html¶

<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post"> # post будет происходить изменения данных на сервере
{% csrf_token %}   # все формы шаблона защита от подделки межсайтовых запросов
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
{% endfor %}
<input type="submit" value="Vote">
</form>

2 Делаем представление Django, которое обрабатывает отправленные данные и что-то с ним делает
polls/views.py # добавляем его 


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice =
question.choice_set.get(pk=request.POST['choice']) 
    except (KeyError, Choice.DoesNotExist)
    # Повторное загрузка окна формы опроса
        return render(request, 'polls/detail.html', { # возвращает словарь со значениями
            'question': question,
            'error_messages': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #Всегда возвращай  HttpResponceRedirect after successfully
        # with post data избегаем повторную публикацию данных
        #user hits the back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id)))     
Разбор:
1 # request.POST['choice'] возвращает индетификатор выбранного варианта строки, всегда возвращает строку

2 # request.POST['choice'] будет вызывать KeyError если ключ choice не был представлен в POST будет повторно отображать форму вопроса
# сообщение об ошибке если choice на задано

3 #  HttpResponseRedirect принимает один аргумент: URL-адрес, на который будет перенаправлен пользователь
#Как указано выше в комментарии Python, вы должны всегда возвращать HttpResponseRedirect после успешной 
# обработки данных POST!!!хорошая практика

4 # функцию reverse() в конструкторе HttpResponseRedirect. Эта функция помогает избежать жесткого кодирования URL-адреса в 
#функции представления. 
# '/polls/3/results/'


3 После того как user проголосовал в опросе представление voice() перенаправляет на страницу результатов для опроса:
polls/views.py

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question}) # rendet то что возвращаем


5 базовые представления: чем меньше кода, тем лучше¶
polls/urls.py¶

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

6 polls/view.py # меняем

class IndexView(generic.ListView): ### Listview
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView): # DetailView  !!!!!
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

1 # По умолчанию базовое представление DetailView использует шаблон с именем <имя приложения>/<имя модели>_detail.html.
#  В нашем случае он будет использовать шаблон "polls/question_detail.html"

2 #Аналогично, базовое представление ListView использует шаблон по умолчанию с именем <имя приложения>/<имя модели>_list.html;
# мы используем template_name, чтобы сказать ListView использовать наш существующий шаблон "polls/index.html".

=====================================================================================================================d

Создание первого приложения на Django, часть 5¶
Тесты

1 Некоторые разработчики на самом деле пишут свои тесты, прежде чем написать свой код

2 полезно написать свой первый тест в следующий раз, когда вы внесете изменение, либо при добавлении
 новой функции или исправлении ошибки.

3 Поиск ошибок 
python manage.py shell

>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # create a Question instance with pub_date 30 days in the future
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # was it published recently?
>>> future_question.was_published_recently()
True

4 Создание тестов 
polls/tests.py

import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

#создали подкласс django.test.TestCase с методом, который создает экземпляр Question с pub_date в будущем.
#Затем мы проверяем вывод was_published_recently() - который должен быть ложным.

5 Исправление ошибки
Question.was_published_recently() должна возвращать false если его pub_date находится в будущем 

polls/models.py

def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

6 Всесторонние тесты
polls/tests.py

def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)

def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)


"""
И теперь у нас есть три теста, которые подтверждают, что Question.was_published_recently() возвращает разумные значения для прошлых,
недавних и будущих вопросов.
"""

7 Тестовый клиент django
>>> responce = client.get('/') !!!!!
 Not Found: /
>>> responce.status_code !!!!
404

1 python manage.py shell

2 >>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
# TIME_ZONE в settings.py проверь

3 >>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()

4 # get a response from '/'
>>> response = client.get('/')
Not Found: /
>>> # we should expect a 404 from that address; if you instead see an
>>> # "Invalid HTTP_HOST header" error and a 400 response, you probably
>>> # omitted the setup_test_environment() call described earlier.
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.urls import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context['latest_question_list']
<QuerySet [<Question: What's up?>]>

7 Улучшение представления 
polls/views.py


    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

# question.objects.filter(pub_date__lte=timezone.now()) возвращает набор запросов, содержащий Question чье pub_date меньше или равно
# то есть раньше или равно timezne.now

=============================================================================

СТАТИКА
1 polls/templates/ # это где хранится html страницы
2 polls/static/polls ### где хранится статика помни надо указывать setings.py
polls/static/polls/style.css. ## как пример
3 polls/style.css ## ссылаться наа этот статический файл в Django можно так


1 polls/static/polls/style.css¶ # пример статики
li a {
    color: green;
}


2 Пример подключение стилей в наш html
polls/templates/polls/index.html
{% load static %} # это тег  генерирует абсолютный URL-адрес статических файлов

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}"> 
# обрати внимание как подключение преоисходит polls/style.css (без полного пути polls/static/polls/style.css!!!!)

3 После чего по следующей ссылке отобразится зеленый цвет
http://127.0.0.1:8000/polls/ ### по ссылке /polls/ # приложение polls

4 Добавление изображения пример
1 polls/static/polls/images ## сюда закидываю картинку 

2 polls/static/polls/style.css¶
body {
    background: white url("images/моя_картинка.gif") no-repeat; #background картинка
}

=================================================
Настройка админки

1 пример админки с множечтво форму
polls/admin.py¶
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']})
        ('Date information', {'fields': ['pub_date']})
    ]
## fieldsets  это первый элемент каждого кортежа 

2 Пример настройки только двух форм:
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text'] ## дата публикации поле текста

admin.site.register(Question, QuestionAdmin)

3 Настройка страницы списка объектов
polls/admin.py¶
class QuestionAdmin(admin.ModelAdmin):
    ######.............
    list_display = ('question_text', 'pub_date')

4 Настройка шаблонов вашего проекта
mysite/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], #### вот эту строку надо добавить обязательно хорошая практика!!!!!!!!!
        'APP_DIRS': True, ## если не сделать то что выше то django просто будет искать по умолчанию подкаталог templates
#DIRS - список каталогов файловой системы, которые нужно проверить при загрузке шаблонов Django; это путь поиска.

5 python -c "import django; print(django.__path__)" # узнать где находится  исходные файлы в Django в вашей системе



6 return как работает

from django.http import HttpResponse

def index(request):
    # Получить HttpRequest - параметр запроса
    # Выполнить операции, используя информацию из запроса.
    # Вернуть HttpResponse 
    return HttpResponse('Hello from Django!') ## HttpRepsponse могу использовать потому что выше его импортировал

 3 render функция #находится в views.py
 Пример

from django.shortcuts import render # импортировал данную функцию
from .models import Team 

def index(request):
    list_teams = Team.objects.filter(team_level__exact="U09")
    context = {'youngest_teams': list_teams}
    return render(request, '/best/index.html', context) ### генерирует html страницу и вернуть ее браузеру учитывая все настройки 
 #которые были указаны ранее и настроены

 sudo dmidecode -t 1




