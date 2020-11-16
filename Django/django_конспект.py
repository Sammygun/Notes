Git Django_app
https://github.com/Sammygun/Django_app
#здесь как создать новый проект или добавить текуший проект
Git
1 git init  ## в папке проекта там где app
Initialized empty Git repository in ~/djangogirls/.git/
2 git config --global user.name "Sammygun" ### пользователь
3 git config --global user.email sam.rybtsov@gmail.com ## почта
4 git status ## смотрю какие изменения были
5 git add --all .
6 git commit -m "Django_app" ## закоммитил изменения дал название изменениям


7  github добавляю на сайте !!!!!!!!!
(setings там можно удалить или переименовать репозиторий)
1 add new Django_app ## на сайте github !!!!!! (галочки можеш не ставить)
none везде добавляй
2 выбирай https 
(…or push an existing repository from the command line)

8 У себя в теривнале 
 git remote add origin https://github.com/Sammygun/Django_app.git
 git branch -M main
 git push -u origin main


9  ЕСЛИ СДЕЛАЛ УЖЕ ИЗМЕНЕНИЯ КАКИЕ НИТЬ на сайте то:
1 git status ## смотрю что поменялось в папке где лежит app
2 git add --all . ## находясь в папке djangogirls
3 git status ### тут увижу что именно будет загружаться
4 git commit -m "Changed the HTML for the site." ### коммитим с заметкой
5 git push ### пушим на gut hub

=========================
SSH аутефикация на github
В самом github в проекте = справо code = тут можно выбрать ssh https

1 ssh-keygen
2 cd .ssh 
3 cat id_rsa.pub копирую все
4 иду на github в правом в верхнем углу user = setings = ssh and gpg keys = new key = название My ssh key = сам ключь вставляй полностью = add new key 
Пример:
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDAmUQ2aCuaaZJPBUbebh2cdXH92ANRiWK2KjQEnK5loltE9LOS6xCJJ4EcUDu/PD+HOFBhSdjeZLkhvdFHb2vh+ihveSQjDuPoFD+3Cp/OMFa3bRQ4H3MYrpv5zyn2WtvPisYjnqyIOJuaHxc7b/fCXdVStMnCCI2JPDIfsBlKDZhHcmUNbwWzkxqnbKD24CJDtNLAHNqjzwDodUOwruuE1n2oDipH3hSL3I9fst+JZ2vHKmWCcJf1RQVRNyiqQcHtmRD+REv1LW4ajIDmLp7wBv4f+jjOjWcIsKmM+O3VxYJFJD9DoQHXyHIyK3L0VQazcF8G1vK7KEMTiCJxZN343zdhARWpAI+PNtpsWR7agVgY5l9HWl7RgKhR+k648sq0yD2rI2+sYznounnT/ak6lTZoIzqbrgQdpvGC2G7UvHFwH+05NuZUbGYoYJ6W8rXWb1rrTq4c18yjl1qrR5gLhR/FWAvxN+H0BWZIRkenNhN9cz8r6p9nl2FJSzZdKDU= sam@sam-Think
5 все теперь когда создаю проект выбираю ssh

6 Если проект уже есть и он работает по https то 
git remote -v # смотрю как проект забрасывается на github
origin  https://github.com/Sammygun/Django_app.git (fetch) # происходит по https
origin  https://github.com/Sammygun/Django_app.git (push)

git remote set-url origin git@github.com:Sammygun/Django_app.git ## меняю с https на ssh 

git remote -v
origin  git@github.com:Sammygun/Django_app.git (fetch) ## все поменялось на ssh
origin  git@github.com:Sammygun/Django_app.git (push)

Проверка работы ssh

7 вношу изменения
1 git status
2 git add . # можно и так 
3 git commit -m "Django_app3_конспект"
4 git push origin



терминал
1 shift + ctrl + t новая вкладка
2 shift + ctrl + w  закрыть вкладку
3 alt 1 , 2 ## переключение между вкладками

https://www.bootstrapcdn.com/ # здесь копирую ссылку css самую первую
bootsrap quick start

Главное пометки
1 python3 manage.py runserver ## запускай в той же директории там где manage.py
http://127.0.0.1:8000/

2 source myvenv/bin/activate #### запустил вирт окружение !!!!!!! 

3 python3 manage.py startapp main ## создаю новое приложение главная страница(main) запускай там где manage.py
#если надо создать forum то так и пишу
app/taskmanager$ ### поэтому пути появиться папка main

4 python3 manage.py startapp main ## создаю новое приложение главная страница запускай там где manage.py
тут же создаться папка с проектом main

5 app/taskmanager/taskmanager$  здесь редактирую файл settings.py
INSTALLED_APPS = [
    'main'
]

6 коментарии в html <!-- текст -->

7 
python3 manage.py makemigrations # в терминале запускаю подготавляю
python3 manage.py migrate ### должно быть все ок если все так то все миграции будут выполнены

8 python3 manage.py createsuperuser
admin
12345 # почту не обязательно в конце спросит точно согласны на легкий пароль да
 http://127.0.0.1:8000/admin/

9 ### суть bootstrap что ты прописываешь специальный class и стили автоматом подтягивются






 1  cd app ## или в папку проекта  или djangogirls
 2 sudo apt install python3-venv## если небыло установлено
 3 python3 -m venv myvenv ## создаем виртуальное окружение 
 4 source myvenv/bin/activate ### в этой же папке запускаем его app
 https://tutorial.djangogirls.org/ru/django_installation/ ## подробно здесь все описано
 5 pip install django ## теперь устанавливаю django работает в виртуальном окружении 
 6 django-admin startproject taskmanager ## стартуем название проекта taskmanager работает в виртуальном окружении
в папке app папка taskmanager # и тут все файлы проекта

drwxrwxr-x 6 sam sam 4096 ноя  6 12:26 myvenv/ # виртуальное окружение
drwxrwxr-x 3 sam sam 4096 ноя  6 12:32 taskmanager/

7 внутри папки taskmanager появиться:
 manage.py* ## поможет запустить локальный сервер, миграции, создание файлов
 # в терминале будем к нему обращаться постоянно но его редактировать не будем
 
 taskmanager/ ## тут будут созданы следующие файлы
 -rw-rw-r-- 1 sam sam  399 ноя  6 12:32 asgi.py
-rw-rw-r-- 1 sam sam    0 ноя  6 12:32 __init__.py
-rw-rw-r-- 1 sam sam 3077 ноя  6 12:32 settings.py ## здесь все настройки нашего проекта
## secret key его можно менять для более высокой безопасности
# DEBUG = True ## режим который во время разработки показывает все ошибки на сайте, но на сервере лучше False
# DATABASES 'django.db.backends.sqlite3' ## можно поменять на другую базу с которой ты хочешь работать
# LANGUAGE_CODE = 'en-us' ## чтобы сайт был на русском языке надо вместо 'en-us' 'ru'

-rw-rw-r-- 1 sam sam  753 ноя  6 12:32 urls.py ## ссылки сайта здесь указываем, urls c путем к шаблону
-rw-rw-r-- 1 sam sam  399 ноя  6 12:32 wsgi.py

8 python3 manage.py runserver ## запускай в той же директории там где manage.py
http://127.0.0.1:8000/ # локальный сервер
## будет ошибка так как мы не провели миграции

9 Приложение
Главная о нас контакты 1 Приложение
форум 2 приложение 

1 python3 manage.py startapp main ## создаю новое приложение главная страница запускай там где manage.py
тут же создаться папка с проектом main

2 app/taskmanager/taskmanager$  здесь редактирую файл settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main' ## просто тут обязательно подключаю свое новое приложение main 
]

10 файлы папки main

-rw-rw-r-- 1 sam sam   63 ноя  6 13:22 admin.py ## здесь можем регить таблицы для админки
-rw-rw-r-- 1 sam sam   83 ноя  6 13:22 apps.py ## спец файл 
-rw-rw-r-- 1 sam sam    0 ноя  6 13:22 __init__.py # в любой проекте есть данный файл
drwxrwxr-x 3 sam sam 4096 ноя  6 13:33 migrations/
миграциии main/migrations
это файлы набор действий что надо сделать с базой данных добавить удалить табличку и т.д. все файлы тут храняться
-rw-rw-r-- 1 sam sam   57 ноя  6 13:22 models.py ### новые таблицы здесь можно создавать для базы данных
drwxrwxr-x 2 sam sam 4096 ноя  6 13:33 __pycache__/
-rw-rw-r-- 1 sam sam   60 ноя  6 13:22 tests.py ## ### также можно создавать здесь тестирование
-rw-rw-r-- 1 sam sam   63 ноя  6 13:22 views.py # здесь указываем как разные страницы будут отображаться
# когда пользователь будет на них заходить зашел на страницу контакты то такой html шаблон


11 связываю taskmanager/urls.py c main/urls.py c папки main

1 taskmanager/urls.py

from django.contrib import admin
from django.urls import path, include # добавляю метод include чтобы  связать main/urls.py 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')) #'' пустая строка, импортированная ранее метод include(добавить) 
    #указываю путь main.urls без точки .py при переходу на страницу main будем вызвать файл utls.py c папки main
]

2 main/urls.py

from django.urls import path 
from . import views ## . точка значит из текущей папки я импортирую файл views.py

urlpatterns = [
    path('', views.index) # обращаюсь к файлу views.py к функции index # '' если перешел на главную то обращаемся к файлу views.py к методу index
]

3 main/views.py

from django.shortcuts import render
from django.http import HttpResponse # для возможности передачи http текста


# Create your views here.
def index(request): # создаю функцию index передаю параметр request метод views.py
    return HttpResponse("<h4>Hello</h4>")         ## возвращаем определенный текст
# к функции index по пути main/views.py обращается main/urls.py

Hello ## вывод на странице локального сервера после обновления страницы 


12 Создаю еще одну страницу
1 main/urls.py

from django.urls import path 
from . import views ## . из этой папки я импортирую файл views.py

urlpatterns = [
    path('', views.index), # обращаюсь к файлу views.py к файлу index 
    path('about-us', views.about), ## еще одна страница о нас сверху , запятая ниже abous_us главное чтобы не было / в начале
# about функция прописана в файле views.py
]

2 main/views.py

from django.shortcuts import render
from django.http import HttpResponse # для возможности передачи текста


# Create your views here.
def index(request): # создаю функцию index передаю параметр request
    return HttpResponse("<h4>Hello</h4>")         ## возвращаем определенный текст

def about(request): # создаю функцию about передаю параметр request
    return HttpResponse("<h4>About</h4>") 

3 Результат 
http://127.0.0.1:8000/about-us ### на серевере появиться ссылка такая
About ## страница с таким значением

13 main/views.py метод render так как HttpResponse # не очень 


1 Создаю в папке main папку templates это папка в которой будут храниться html шаблоны приложения main.
В папке templates папку создать main названия приложения !!!!!!!!!
main/templates/main ### вот такие папки создаются 
#удобная структура каждое приложение имеет свое шаблоны чтобы не было путаницы

В этой папке создаю файл index.html ### так как это главная страница
title прописываю главная страница en меняю на ru

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Главная страница</title>
</head>
<body>
    <h1>Главная страница</h1>
    <p>Просто текст</p>

</body>
</html>





2 main/views.py # связываю с html шаблоном созданным выше

from django.shortcuts import render
from django.http import HttpResponse # для возможности передачи текста


# Create your views here.
def index(request): # создаю функцию index передаю параметр request
    return render(request, 'main/index.html')## возвращаем лучше render в скобках request, шаблон html
# ты путь к шаблону как будту ты уже в templates поэтому просто main/index.html

def about(request): # создаю функцию about передаю параметр request
    return HttpResponse("<h4>About</h4>") 

## выведит страницу главная просто текст
вывод:
1 urls.py ## это пути сайта ссылки
2 views.py # это то как будет выглядить сайт
3 templates/main # это где мы создаем шаблоны страниц index.html потом прописываем их в views.py 


3 создаю шаблон для страницы about
1 main/views.py


from django.shortcuts import render
from django.http import HttpResponse # для возможности передачи текста


# Create your views here.
def index(request): # создаю функцию index передаю параметр request
    return render(request, 'main/index.html')## возвращаем лучше render в скобках request, шаблон html
# ты путь к шаблону как будту ты уже в templates поэтому просто main/index.html

def about(request): # создаю функцию about передаю параметр request
    return render(request, "main/about.html")  ## ссылку на шаблон templates/main/about.html


2 templates/main/about.html создаю шаблон 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Страница про нас</title>
</head>
<body>
    <h1>Страниц про нас</h1>
    <p>Страница про нас</p>
</body>
</html>

### вывод страницы
<h1>Страниц про нас</h1>
    <p>Страница про нас</p>



14 добавление bootsrap стилей
https://www.bootstrapcdn.com/ ## здесь копируюю ссылку css первую

вставляю в index.html about.html так:
    <title>Главная страница</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
about.html
    <title>Страница про нас</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

15 Захожу на сайт официальный https://getbootstrap.com/
Examples = выбирай pricing = просмотреть в chrome (режим разработки) =  выбири галочку мышки 
= выбери самый вверх Company name = div class светанет = правой кнопкой = Copy = Copy element=
и вставь в свой about.html в body
https://getbootstrap.com/docs/4.5/examples/pricing/

вставляю в index.html about.html так:
коментарии в html <!-- -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Страница про нас</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
        <h5 class="my-0 mr-md-auto font-weight-normal">itProger</h5>
        <nav class="my-2 my-md-0 mr-md-3">
          <a class="p-2 text-dark" href="/">Главная</a> # будет кидать на главную 
          <a class="p-2 text-dark" href="/about-us">Про нас</a> <!--ссылка на страницу about-us-->
        </nav>
    </div>
    <h1>Страниц про нас</h1>
    <p>Страница про нас</p>
</body>
</html>

16 Убираем повторяющийся код dont repeat yourself
Dont repeat yourself
1 По пути:
taskmanager/main/templates/main ## место где хранятся html шаблоны приложения main создаю base.html
base.html # аккуратней скоментами html python их видит

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title> <!--блок менющийся title название-->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<body>
    <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
        <h5 class="my-0 mr-md-auto font-weight-normal">itProger</h5>
        <nav class="my-2 my-md-0 mr-md-3">
          <a class="p-2 text-dark" href="/">Главная</a>
          <a class="p-2 text-dark" href="/about-us">Про нас</a>
        </nav>
    </div>

    {% block content %}{% endblock %} <!--блок менющийся title название-->
</body>
</html>

<!--Суть в том что мы удаляем все что будет меняться, то что не будет остается-->
<!--{% block title %}{% endblock %} ### то что будет меняться-->

2 main/templates/main
about.html # подключаею шаблон base.html
{% extends 'main/base.html' %}

{% block title %}
Страница про нас ## указываю что хочу видеть в блоке title его место указано в base.html
{% endblock %}

{% block content %}
<h1>Страниц про нас</h1>
<p>Страница про нас</p>## указываю что хочу видеть в блоке title его место указано в base.html
{% endblock %}

2 main/templates/main/index.html


{% extends 'main/base.html' %}

{% block title %}
Главная страница
{% endblock %}

{% block content %}
<h1>Главная страница</h1>
<p>Просто текст</p>
{% endblock %}

Суть в том, что html который не меняется мы не трогаем  а то что нам надо поменять мы ссылаемся на base.html 
где есть название блоков которые нужно менять в самом файле index.html мы их меняем но весь html не нужен

17 Работа в base.html

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title> <!--блок менющийся title название-->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<body>
    <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
        <h5 class="my-0 mr-md-auto font-weight-normal">itProger</h5>
        <nav class="my-2 my-md-0 mr-md-3">
          <a class="p-2 text-dark" href="/">Главная</a>
          <a class="p-2 text-dark" href="/about-us">Про нас</a>
        </nav>
    </div>
<div class="container"> ## указал класс bootstrap 
    {% block content %}{% endblock %}  #обвернул и контент теперь у меня централизуется уже на всех страницах
</div>

</body>
</html>

Суть в том что меняю стили и инфу в base.html  меняется все страницы на лету about-us, main


18 Правильное указание ссылок в django
1 main/urls.py

from django.urls import path 
from . import views ## . из этой папки я импортирую файл views.py


urlpatterns = [
    path('', views.index, name='home'), # нужно указывать параметр name  с указанием названия  
    path('about-us', views.about, name='about' ), 
]

2 main/base.html


<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title> <!--блок менющийся title название-->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<body>
    <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
        <h5 class="my-0 mr-md-auto font-weight-normal">itProger</h5>
        <nav class="my-2 my-md-0 mr-md-3">
          <a class="p-2 text-dark" href="{% url 'home' %}">Главная</a>#самое главное названия указываем с urls.py 
          <a class="p-2 text-dark" href="{% url 'about' %}">Про нас</a>### !!!!!!!
        </nav>
    </div>
<div class="container">
    {% block content %}{% endblock %} 
</div>

</body>
</html>

Такая концепция связана с тем, что если я зайду в main/urls.py
urlpatterns = [
    path('', views.index, name='home'), # нужно указывать параметр name  с указанием названия  
    path('about', views.about, name='about' ), #!! здесь поменяю  вместо about-us about ничего не полетит
]

href="{% url 'home' %}" ## когда в base.html так прописываем то мы можем легко менять название страницы в 
# urls.py

19 создаю базу данных захожу в main/models.py

from django.db import models

class Task(models.Model): # создаю таблицу Task
    title = models.CharField('Название', max_length=50)  ## первое поле в базе данных
    # обращаюсь к models потом иду к специальному классу CharField даю название Название, для маленьких полей
    task = models.TextField('Описание') ## TextField для больших полей используется  

    def __str__(self): ## тут аккуратней с пробелами после def
        return self.title

python3 manage.py makemigrations # в терминале запускаю
Migrations for 'main':
  main/migrations/0001_initial.py ## путь где лежит миграция
    - Create model Task ### таблица Task создана 

Делаю уже саму миграцию
python3 manage.py migrate ### должно быть все ок

20 Создаю администратора для админки 
create super user
админка /admin

в терминале создаю пользователя
1 python3 manage.py createsuperuser
admin
12345 # почту не обязательно, в конце спросит точно согласны на легкий пароль да
http://127.0.0.1:8000/admin/
users # здесь создаем новых пользователей добавляем  и т.д. меняем им пароль

21 добавляю таблицу task
main/admin.py ## тут ее надо добавлять

from django.contrib import admin
from .models import Task # с models.py импортирую то что прописывали выше

admin.site.register(Task) # admin импортирован выше  .site(сайт) .register функция регистрируем таблицу Task

в админке появиться приложение main Task
main Task =  добавить = купить молоко название = Описание не забудь купить молока
main Task =  добавить = купить машину = Ну попробуй ## можно потом менять 

21 Хочу переименовать таблицу с task в задачи в самой админке
main/models.py 

from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50) 
    task = models.TextField('Описание')  

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача' # в единственном числе !!! переименование в админке !!!
        verbose_name_plural = 'Задачи' # в множественном числе


В самой адмнке появиться Задачи вместо Tasks, каждая запись будет именоваться в Задача

22 Нам надо чтобы все наши Task(Задачи) выводились на сайте которые есть в админке про молоко и машину
1 main/views.py

from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all() # до отображения создаем переменную tasks = Task(model) (objests)объекты.allвсе
    # то что с в models.py  мы класс создавали
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})
    ## возвращаем лучше render в скобках request, шаблон html
# ты путь к шаблону как будту ты уже в templates поэтому просто main/index.html
# меняем главную страницу создаю словарь {'title': 'Главная страница сайта', 'tasks': tasks})
def about(request): # создаю функцию about передаю параметр request
    return render(request, "main/about.html")  ## ссылку на templates/main/about.html

2 нахожу верстку index.html
templates/main/index.html # 


{% extends 'main/base.html' %}

{% block title %}
{{ title }} # ссылаюсь на views.py title смотри словарь выше в заголовке Главная страница сайта появиться
{% endblock %}

{% block content %}
<h1>Главная страница</h1>
<p>Просто текст</p>
{% endblock %}

3 меняю index.html чтобы значения models.py (адинка значения отображались в на главной странице)
main/index.html

{% extends 'main/base.html' %}

{% block title %}
{{ title }}
{% endblock %}

{% block content %}
<h1>Главная страница</h1>
{% for el in tasks %} # el #element в словаре tasks
    <div class="alert alert-warning mt-2"> # стиль bootstrap
        <h3>{{ el.title }}</h3> # обращаюсь к title #обращение к models.py title где была описана модель
        <p>{{ el.task }}</p> # обращаюсь к task #обращение к models.py task
    </div>
{% endfor %} # закрываю цикл
{% endblock %}

# коментарии в этом файле не работают !!!!!


23 main/views.py типо сортировки записей с базы данных
tasks = Task.objects.all() # до отображения создаем переменную tasks = Task(model) (objests)объекты.allвсе
tasks = Task.objects.order_by('id') # сортировка по 'id', или можно по полю 'title', 'tasks' описанных в models.py
tasks = Task.objects.order_by('-id') # будет от старой записи к новой удобно в блоге новые вверху 
tasks = Task.objects.order_by('-id')[:1] # делаю ограничение чтобы только отображался один элемент
# -id отображение со старой к новой с последней к новой [:1] # ограничение ток одна запись


24 Ставим условие которое сработает если у нас записей не будут
main/index.html


{% extends 'main/base.html' %}

{% block title %}
{{ title }}
{% endblock %}

{% block content %}
<h1>Главная страница</h1>
{% if tasks %} ### создаем условие что если чего нету
{% for el in tasks %} 
    <div class="alert alert-warning mt-2">
        <h3>{{ el.title }}</h3>
        <p>{{ el.task }}</p>
    </div>
{% endfor %}
{% else %} ## то тогда возвращаюм такую запись
    <p>У нас нет записей</p>
{% endif %}
{% endblock %}


25 
1 main base.html страницу добавим для редактирования записей
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title> <!--блок менющийся title название-->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<body>
    <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
        <h5 class="my-0 mr-md-auto font-weight-normal">itProger</h5>
        <nav class="my-2 my-md-0 mr-md-3">
          <a class="p-2 text-dark" href="{% url 'home' %}">Главная</a>
          <a class="p-2 text-dark" href="{% url 'about' %}">Про нас</a>
          <a class="p-2 text-dark" href="{% url 'create' %}">Создать таск</a> ## вот эту запись добавим
        </nav>
    </div>
<div class="container">
    {% block content %}{% endblock %} 
</div>

</body>
</html>

2 main/urls.py
Помни если создал в base.html новую страницу обязательно забегай сюда на base.html

from django.urls import path 
from . import views ## . из этой папки я импортирую файл views.py


urlpatterns = [
    path('', views.index, name='home'),  
    path('about-us', views.about, name='about'), 
    path('create', views.create, name='create'),# добавим отслеживание новой страницы create base.html
    # везде create однако метода views.create поэтому идем views.py
]

3 захожу в main/views.py создаю метод create внизу в самом

from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id') # до отображения создаем переменную tasks = Task(model) (objests)объекты.allвсе
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})
    ## возвращаем лучше render в скобках request, шаблон html
# ты путь к шаблону как будту ты уже в templates поэтому просто main/index.html
# меняем главную страницу создаю словарь {'title': 'Главная страница сайта', 'tasks': tasks})
def about(request): # создаю функцию about передаю параметр request
    return render(request, "main/about.html")  ## ссылку на templates/main/about.html


def create(request): # создаю метод create передаю параметр request !!!!!!
    return render(request, "main/create.html")  ## ссылку на templates/main/create.html!!!!


4 теперь templates/main/ создаю шаблон create.html

{% extends 'main/base.html' %}

{% block title %}
Создать таск
{% endblock %}

{% block content %}
<h1>Создать таск</h1>
<form method="POST"> ## создаю форму
    <input type="text" placeholder="Введите название" class="form-control"><br> #поле оглавление
    <textarea placeholder="Введите описание" class="form-control"></textarea><br># место text area
    <button type="submit" class="btn btn-success">Добавить</button> #кнопка добавить
</form>
{% endblock %}

### суть bootstrap что ты прописываешь специальный class и стили автоматом подтягивются

5 Если нажать кнопку Добавить будет ошибка, исправляем данную проблему
в папке приложения просто main (без templates) создаем новый файл forms.py
main/forms.py

from .models import Task ## импортирую с models.py модель Task
from django.forms import ModelForm ## добавляю класс

class TaskForm(ModelForm): #TaskForm название формы импортируем ModelForm 
    class Meta:
        model = Task
        fields = ["title", "task"] ## поле которые должны быть в форме беру название models.py
        # title название формы, task описание

6 перехожу templates/main/create.html

{% extends 'main/base.html' %}

{% block title %}
Создать таск
{% endblock %}

{% block content %}
<h1>Создать таск</h1>
<form method="POST">
    {% csrf_token %}  ## спецключь чтобы форма работала без нее не будет отправка, что формачка отправляла
    <input type="text" placeholder="Введите название" class="form-control"><br>
    <textarea placeholder="Введите описание" class="form-control"></textarea><br>
    <button type="submit" class="btn btn-success">Добавить</button>
</form>
{% endblock %}

7 захожу main/views.py 

from django.shortcuts import render
from .models import Task
from .forms import TaskForm # импортирую с текущей папки с forms.py объект TaskForm !!!! 


def index(request):
    tasks = Task.objects.order_by('-id') # до отображения создаем переменную tasks = Task(model) (objests)объекты.allвсе
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})
    ## возвращаем лучше render в скобках request, шаблон html
# ты путь к шаблону как будту ты уже в templates поэтому просто main/index.html
# меняем главную страницу создаю словарь {'title': 'Главная страница сайта', 'tasks': tasks})
def about(request): # создаю функцию about передаю параметр request
    return render(request, "main/about.html")  ## ссылку на templates/main/about.html


def create(request): # создаю метод create передаю параметр request !!!!!!
    form = TaskForm() # переменная form ссылается объект TaskForm forms.py!!!!!
    context = {
        'form': form # ключ form
    } # создаю словарь
    return render(request, "main/create.html", context)  ## ссылку на templates/main/create.html
    #ссылаюсь на словарь context !!!!!

    8 main/create.html

    {% extends 'main/base.html' %}

{% block title %}
Создать таск
{% endblock %}

{% block content %}
<h1>Создать таск</h1>
<form method="POST">
    {% csrf_token %} 
    {{ form.title }} ## указываю form.title c forms.py
    {{ form.task }} ## указываю task c forms.py
    <input type="text" placeholder="Введите название" class="form-control"><br>
    <textarea placeholder="Введите описание" class="form-control"></textarea><br>
    <button type="submit" class="btn btn-success">Добавить</button>
</form>
{% endblock %}

Появиться рабочие поля которые будут рабочими но у них нету стилей, их надо связать с полями которые имеют 
стили bootsrap


9 forms.py
связываю поля рабочие с красивыми полями

from .models import Task 
from django.forms import ModelForm, TextInput, Textarea ## подключаю класс TextInput 

class TaskForm(ModelForm):  
    class Meta:
        model = Task
        fields = ["title", "task"] 
        widgets = {
            "title": TextInput(attrs={ ##attrs атрибут словарь в словаре
                'class': 'form-control', ## верстка с create.html
                'placeholder': 'Введите название' ## также
            }),
            "task": Textarea(attrs={ ##attrs атрибут словарь в словаре для task
                'class': 'form-control', ## верстка с create.html
                'placeholder': 'Введите описание' ## также c поля task
            }),    
        } # создаю словарь и в нем создаю объект TextInput


10 потом захожу в create.html 
то что делал выше в forms.py просто связывал cвои поля с  title task передав им атрибуты 
{% extends 'main/base.html' %}

{% block title %}
Создать таск
{% endblock %}

{% block content %}
<h1>Создать таск</h1>
<form method="POST">
    {% csrf_token %} 
    {{ form.title }}<br> ## # вот это в forms.py связывал с версткой, которая здесь ниже 
    {{ form.task }}<br> # br отступ 
 #   <input type="text" placeholder="Введите название" class="form-control"><br>
 #  <textarea placeholder="Введите описание" class="form-control"></textarea><br>
#  <button type="submit" class="btn btn-success">Добавить</button>
# это коменчу так как нам эти поля не нужны
</form>
{% endblock %}


11 Однако формы ничего не отправляют
views.py
from django.shortcuts import render, redirect # метод redirect
from .models import Task
from .forms import TaskForm # импортирую с текущей папки с forms.py объект TaskForm


def create(request): # создаю метод create передаю параметр request
    if request.method == 'POST': # если метод Post
        form = TaskForm(request.POST) # получаем
        if form.is.valid():## если данные корректы проверяйм при помощий функции .is.valid 
            form.save() # тогда мы их сохраняем
            return redirect('home') ###выходим из функции и возвращаем переадресуем пользователя на другую страницу
        else: ### если форма не корректна то 
            error = "Форма была неверной"

    form = TaskForm() # переменная form ссылается объект TaskForm forms.py!!!!!
    context = {
        'form': form # ключ form
        'error': error
    } # создаю словарь
    return render(request, "main/create.html", context)  ## ссылку на templates/main/create.html
    #ссылаюсь на словарь context

12 error добавим на create.html

{% extends 'main/base.html' %}

{% block title %}
Создать таск
{% endblock %}

{% block content %}
<h1>Создать таск</h1>
<form method="post">
    {% csrf_token %} 
    {{ form.title }}<br>
    {{ form.task }}<br>
    <button type="submit" class="btn btn-success">Добавить</button>
    <span>{{ error }}</span> ## добавил вывод об ошибке
</form>
{% endblock %}



