Проблемы были на странице Динамически изменяющиеся данные в шаблонах

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

4 
mysite/urls.py
from django.contrib import admin
from django.urls import path, include # функция include будет использована ниже поэтому ссылаемся на нее

    path('admin/', admin.site.urls),
#Таким образом, любому URL-адресу, начинающемуся с admin/, Django будет находить соответствующее view (представление view.py).!!!
    path('', include('blog.urls')), ## здесь ссылаемся на blog.urls (blog/urls.py)

5 blog/urls.py ## создаю пустой данный файл
from django.urls import path ## path функцию которую импортировали
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list') #'' # пустая строка
    # views.post_list — это правильное направление для запроса к твоему веб-сайту по адресу 'http://127.0.0.1:8000/'.
]   # name='post_list' это имя URL, которое будет использовано, чтобы идентифицировать его


6 view это представление здесь мы представляем что от чего будет отдаваться клиенту в зависимости от обращения к определенной страницы


blog/views.py
from django.shortcuts import render # импортируем функцию render

def post_list(request):
    return render(reques, 'blog/post_list.html', {}) ## blog/template/blog хранилка html шаблонов
    #ссылаемся на возврат конкретного шаблона

#функцию (def) с именем post_list, которая принимает request в качестве аргумента и возвращает (return) результат
#  работы функции render, которая уже соберёт наш шаблон страницы blog/post_list.html.

7 Шаблон html к примеру шаблон письма который ты не хочешь постоянно набирать
blog/templates/blog # хранилка шаблонов приложения blog
post_list.html # тут создаю html шаблон


8 базовый html 
<h1>Заголовок</h1> — главный заголовок страницы;
<h2>Подзаголовок</h2> — для заголовков второго уровня;
<h3>Заголовок третьего уровня</h3> … и так далее, вплоть до <h6>;
<p>A paragraph of text</p>
<em>текст</em> подчёркивает твой текст;
<strong>текст</strong> — жирный шрифт;
<br /> — переход на следующую строку (внутрь br тега нельзя ничего поместить);
<a href="https://djangogirls.org">link</a> создаёт ссылку;
<ul><li>первый элемент</li><li>второй элемент</li></ul> создаёт список, такой же как этот!
<div></div> определяет раздел страницы.


9 django командная строка 

1 python manage.py shell ## вызов консоли

2 from blog.models import Post # делаем импорт объекта Post описанный в models.py
3 Post.objects.all() ## смотрю все посты объекта Post

4 Post.objects.create(author=me, title='Sample title', text='Test') # передаю объект Post в базе данных
""" create создать (автор переменная me, title(свойство объекта Post в models.py, заголовок Sample title,))
text 3 свойство объекта Post, просто пишем Test
me это переменная нам нужно импортировать нашего пользователя и присвоить ему значение
"""
4.1 from django.contrib.auth.models import User # импортирую пользователя
4.2 User.objects.all() ## нахожу суперпользователя
""" мы получили (get) пользователя (User) с именем username 'ola' """

4.3 me = User.objects.get(username='admin')

4.4. Post.objects.create(author=me, title='Sample title', text='Test') # создаю запись в базе данных с переменной me
 <Post: Sample title>

4.5 Post.objects.all() # смотрю все записи объекта Post описанного в models.py
# все публикации сделаны при помощи объекта Post


9.2 фильтрация объектов в консолои django
1  Post.obects.filter(author=me) ## смотрю публикации конкретного пользователя

2 Post.objects.filter(title__contains='title')
""" в поле title класса  Post ищу слова title """

3 from django.utils import timezone # если хотим получить список опубликованных записей по полю published_date
Post.objects.filter(published_date__lte=timezone.now())

4 post = Post.objects.get(title="Sample title") ### публикуем конкретную запись объекта Post c заголовком Sample title
""" присваимваем переменную post к нашей публикации"""

5 post.publish() ##публикую нашу переменную post со значением  нашей записи Sample title

6 Post.objects.filter(published_date__lte=timezone.now())

9.3 Сортировка объектов
1 Post.objects.order_by('created_date')## сортирую по полю created_date
2 Post.objects.order_by('-created_date') ### тоже самое только задом наперед

9.4 Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
сцепил что вывожу по полю published_date  и сортирую по полю published_date 
# published_date (смотри models.py)
exit() # выхожу


10 Динамически изменяющиеся данные в шаблонах
blog/views.py
from django.shortcuts import render
from .models import Post # . текущая директория models без py класс Post
""" Данная запись говорит от том что мы импортируем из models.py объект Post в views.py  """

def post_list(request):
    return render(request, 'blog/post_list.html', {})

10.1 Опять меняем blog/views.py
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
""" то что вводил в терминале присвоил значение переменной  posts Post объект (models.py) фильтр
по полю published_date (смотри models.py) и сортируем данное поле, переменная posts добавляем"""


11 Шаблоны Django
Django имеет теги которые позволяют создавать вставлять python в html, так браузер не поймет так как он не знает python
blog/templates/blog/post_list.htm 
{{ posts }} ##пример установки переменной в шаблон 


12 css в Django 
blog/templates/blog/post_list.html
1 head
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
head
'''Подключаю bootstrap '''

2 blog/static/css/blog.css ## создаю файл для стилей 
h1 a {
    color: #FCA205; # меняю цвет 
} 
3 blog/templates/blog/post_list.html # подключаем статику 
{% load static %} ## в самом вверху
head
<link rel="stylesheet" href="{% static 'css/blog.css' %}">
head

Итого должно быть вот так 
    <head>
        <title>Django Girls blog</title>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        <link href="https://fonts.googleapis.com/css?family=Lobster&subset=latin,cyrillic" rel="stylesheet" type="text/css">
        <link rel="stylesheet" href="{% static 'css/blog.css' %}"> ### подключение статики в  самом внизу
    </head>


    13 Создаем шаблон 
 1   blog/templates/blog/base.html

    {% load static %}
<html>
    <head>
        <title>Django Girls blog</title>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        <link href='//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    </head>
    <body>
        <div class="page-header">
            <h1><a href="/">Django Girls Blog</a></h1>
        </div>
        <div class="content container">
            <div class="row">
                <div class="col-md-8">
                {% block content %}
                {% endblock %}
                </div>
            </div>
        </div>
    </body>
</html>
## {% block content %} то что выше это цикл который у нас указан в post_list.html
#{% endblock %}

2 blog/templates/blog/post_list.html 
{% for post in posts %}
    <div class="post">
        <div class="date">
            {{ post.published_date }}
        </div>
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.text|linebreaksbr }}</p>
    </div>
{% endfor %}
# то что пойдет в между {% block content %} и {% endblock %} в blog/templates/blog/base.html

14 Создаем в шаблоне ссылку на страницу поста
blog/templates/blog/post_list.html

{% extends 'blog/base.html' %}

{% block content %}
    {% for post in posts %}
        <div class="post">
            <div class="date">
                {{ post.published_date }}
            </div>
            <h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaksbr }}</p>
        </div>
    {% endfor %}
{% endblock %}

# <h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
{% %} # теги шаблонов Django
Параметр post_detail означает, что Django будет искать URL с именем post_detail в файле blog.urls.py.

А что насчёт pk=post.pk? pk — это сокращение от primary key (первичный ключ). Он уникальным образом определяет каждую запись в базе данных. 
Поскольку мы не задали первичного ключа в нашей модели Post, Django создал такой ключ за нас (по умолчанию это порядковый номер, то есть 1, 2, 3…)
 и добавил поле pk к каждой записи блога. Для получения первичного ключа мы напишем post.pk — точно так же, как мы получали значения остальных полей 
 (title, author и т.д.) нашего объекта Post.

 14.1  blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

# post/<int:pk>/ определяет шаблон URL-адреса  ## указываем какой шаблон должен открыться по определенной ссылке


14.2 blog/views.py
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

14.3 blog/templates/blog/post_detail.html
{% extends 'blog/base.html' %}

{% block content %}
    <div class="post">
        {% if post.published_date %}
            <div class="date">
                {{ post.published_date }}
            </div>
        {% endif %}
        <h1>{{ post.title }}</h1>
        <p>{{ post.text|linebreaksbr }}</p>
    </div>
{% endblock %}

15 blog/forms.py

from django import forms ## импортируем формы

from .models import Post ## импортирую нашу модель Post

class PostForm(forms.ModelForm):
    """ PostForm, как ты, вероятно, подозреваешь, — это имя для нашей формы. Нам нужно также сообщить Django, что эта форма 
    относится к ModelForm (forms.ModelForm) """

    class Meta:
        model = Post
        fields = ('title', 'text',)
        """мы можем указать, какие поля должны присутствовать в нашей форме. Сейчас нам требуются только поля title и text — author"""

16 
blog/templates/blog/base.html
{% load static %}
<html>
    <head>
        <title>Django Girls blog</title>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        <link href='//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    </head>
    <body>
        <div class="page-header">
            <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
            <h1><a href="/">Django Girls Blog</a></h1>
        </div>
        <div class="content container">
            <div class="row">
                <div class="col-md-8">
                    {% block content %}
                    {% endblock %}
                </div>
            </div>
        </div>
    </body>
</html>

16.1 
blog/urls.py
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]

16.2 
blog/views.py
from .forms import PostForm
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

Чтобы создать новую форму Post, нам потребуется вызвать PostForm() и передать её шаблону.
Мы ещё вернёмся к этому представлению, а пока давай быстро создадим шаблон под форму.

16.3
blog/templates/blog/post_edit.html
{% extends 'blog/base.html' %}

{% block content %}
    <h1>New post</h1>
    <form method="POST" class="post-form">{% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="save btn btn-default">Save</button>
    </form>
{% endblock %}

16.4 
blog/views.py
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

16.5 
blog/views.py
def post_new(request):
    if request.method == "POST": ## цикл 
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

16.6 
blog/templates/blog/post_detail.html
{% extends 'blog/base.html' %}

{% block content %}
    <div class="post">
        {% if post.published_date %}
            <div class="date">
                {{ post.published_date }}
            </div>
        {% endif %}
        <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
        <h1>{{ post.title }}</h1>
        <p>{{ post.text|linebreaksbr }}</p>
    </div>
{% endblock %}

16.7
blog/views.py
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    """ Выглядит практически идентично представлению post_new, верно? Но не совсем. Во-первых, мы передаём параметр pk из URL-адреса.
     Кроме того, мы получаем модель Post для редактирования при помощи get_object_or_404(Post, pk=pk)
      и передаём экземпляр post в качестве instance форме и при сохранении…"""


16.8 Безопасность

blog/templates/blog/post_detail.html
{% if user.is_authenticated %} # чел увидет на странице только если он авторизовался
     <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
{% endif %}