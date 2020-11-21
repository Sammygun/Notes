

vs code настройка
Урок 6 python extension и далее остановка на 8
 ctrl + ` ### вызов терминал в vscode также переключение между текстом и терминалом
 ctrk + b #боковая панель убрать поставить
 ctrl + tab ## переключение 
1 расширения =  python = install потом просто перезагрузи его

2 в правом нижнем углу vs code выберите интерпретатор
python 3.8 выбери 
справо появиться уведомление установите linter pylint позволяет видеть ошибки до запуска кода
ctrl + shift + m ### позволяет увидеть есть ли проблемы панель problems снизу view = problems

3 view = command palette =  ctrl + shift + p = lint = все команды lint (возможно надо выбрать on) = select linter = выбери pylint (самый популярный)

4 настройка шрифта = справо внизу шарнир = setings = text editor = font size 21 
настройки шрифта терминала = справо внизу шарнир = setings = features = terminal = font size 18 

5 русификация
плагин Russian Language Pack for Visual Studio Code установи его

6 настройка github
https://habr.com/ru/post/490754/#github

7 проблема с курсором исчезает при alt - shift смене языка просто меняю на ctrl + shift
https://ru.stackoverflow.com/questions/901929/vs-code-%D0%BE%D1%82%D0%BA%D0%BB%D1%8E%D1%87%D0%B8%D1%82%D1%8C-%D0%BA%D0%BB%D0%B0%D0%B2%D0%B8%D1%88%D1%83-alt
нlастройки = параметры = окно = custom menu bar alt focus (в поиске menu) галочку сними и alt  появиться

8 правой кнопкой мыши  слева меню add folder можно добавить

9 ctrl + h ## можно переименовать все переменные в коде  !!!

10 вернуть верхнию панель меню 
alt = вид = внешний вид = показать строку меню
=================================================================
Установка python.org = нажимаю downloads =желтакая кнопка  download python = перед установкой нажми обязательно галочку add Python 3.7. to Path
потом pycharm на оф сайте = community он бесплатен


crtl + j это с новой строки
shft + @ это кавычки """"
решетка shift 3 #
одинарные кавычки просто кнопка @
| shift + решетка
| shift \
* shift + 8
& shift + 7
кавычки просто  латиницей ё кнопка `````
shift + ё ~

# shift + 3
: shift + возле L
pycharm масштабирование текста view = toolbar = setings=font=
вверху setings  гаечный ключ = font = size 30
https://www.youtube.com/watch?v=OjLsJJVB_AE

изменение переменных правой кнопкой маши refactor = rename вводишь и все
или Shift + F6

ctrl + Tab переключение между вкладками


$ shift + 4

создание новой директории = New direction=ecommerce
в ecommerce создаю новый файл __init__.py

https://docs.python.org/3/py-modindex.html
модули все в python



==============================================================

1 ctrl shift p поисковик в visual studio code
в папке открыть окно команд shift правой кнопкой мыши а там уже дописывай файл

2 ctrl + SHIFT + P     Палитра команд = format Document install его проверка на pep 8

потом когда пишешь код SHIFT + ALT + F автоматически установит все по данному стандарту

CTRL + ,  параметры = в поиске = format on save = галочку теперь Pep 8 будет постоянно исправлят все при сохраниении


3
ctrl + `  это терминал встроенный
потом python app.py и все сработает или на маке $python3 app.py
но есть расширение code runner .run установи его перезапусти vs code
Сначало SAVE сохраняй код = потом CTRL ALT N и программа автоматически загрузиться, но в начале сохрани иначе ничего не сработает

ctrl + ` (ё)  запуск терминал
cd B:
python app.py   # запуск приложения


ctrl + = увеличить масштаб
ctrl + - уменьшить масштаб
Настройка шрифта = Параметры = текстовый редасктор = шрифт= размеры шрифта = font size 24s
ctrl + SHIFT + P     Палитра команд
ctrl + SHIFT + M   Проблемы посмотреть



=====================================================
Важные заметки примеры
1 
course = "Python Programming"
print(len(course))  # 18
print(course[0])  # P
print(course[-1])  # g
print(course[0:3])  # Pyt ### будет выводить с индексом 0 1 2, поэтому Pyt 
print(course[0:])  # Python Programming c первой до последней
print(course[:3])  # Pyt также будет
print(course[:]) # Python Programming

2
for x in range(5): # x
    for y in range(3):  # y
        print(f"({x}, {y})")

(0, 0)      # помни сначало от 0 до 4 (range (5)) # потому что отсчет от от 0?
(0, 1)        # помни сначало от 0 до 2 (range (3))
(0, 2)     #идет сначало 0 (и так до 4(5 не входит)) прогоняется до 2 (3 не входит в это число)
(1, 0)    # потом идет 1 прогоняется до 2 (3 не входит) и так до 4 (5 не входит)
(1, 1)
(1, 2)
(2, 0)
(2, 1)
(2, 2)
(3, 0)
(3, 1)
(3, 2)
(4, 0)
(4, 1)
(4, 2)


lesson 5

mystring = "Bla bal bal"
name = "mr vasya pupkin"
print(name.title()) # ставит только заглавные буквы
#Mr Vasya Pupkin
print(name.upper())  # все с большой буквы становится
#MR VASYA PUPKIN
print(name.lower()) # все с маленькой буквы

print("Privet\nPrivet\n\nStroka 3") # c красной строки
print("Messages1:\n\tMessages\n\tMessages2\n\tMessages3")
# Делаю с новой строки и делаю t-TAB
#Messages1:
#    Messages
#    Messages2
#    Messages3
print("lower name:" + name.lower())
# lower name:mr vasya pupkin вывод
a = " . , dadya vasya .  "
print(a)
print(a.rstrip())#стирает пробел справо чисто в самом начале
print(a.lstrip())# стирает пробел Left слево чисто в самом начале
print(a.strip()) # подрезаем сразу пробелы с двух сторон

a = "..... dadya vasya ...."
a = a.strip(".") # udalenie tochek
a = a.strip()  # udalenie probelov
print(a.title()) # пишу чтоб были  заглавные
#Dadya Vasya

VS code  два раза на два файла нажимаю и меню скрывается
New Folder open , create app.py

_______________________________________
MOSH
2 >1 True   (Yes)
2 > 4 False  (NO)

https://www.python.org/dev/peps/pep-0008/
pep 8 Стандарт написания на данном языке
ctrl + SHIFT + P     Палитра команд = format Document install его проверка на pep 8

потом когда пишешь код SHIFT + ALT + F автоматически установит все по данному стандарту

CTRL + ,  параметры = в поиске = format on save = галочку теперь Pep 8 будет постоянно исправлят все при сохраниении




Функции это как пульт с конпками
ctrl + `  это терминал встроенный
потом python app.py и все сработает или на маке $python3 app.py
но есть расширение code runner .run установи его перезапусти vs code
Сначало SAVE сохраняй код = потом CTRL ALT N и программа автоматически загрузиться, но в начале сохрани иначе ничего не сработает

ctrl + ` (ё)  запуск терминал
cd B:
ls работает
cd HelloWorld
python app.py   # запуск приложения


ctrl + = увеличить масштаб
ctrl + - уменьшить масштаб
Настройка шрифта = Параметры = текстовый редасктор = шрифт= размеры шрифта = font size 24s
ctrl + SHIFT + P     Палитра команд
ctrl + SHIFT + M   Проблемы посмотреть



print("Hello World")
print("*" * 10)            10 раз умножу *
___________________________________________________
2 lesson
students_count = 1000 #int
rating = 4.99 #float
is_published = False #bollean
cousre_name = "Python Programming"# строка обязательно в кавычках
print(students_count)

____________________________________________
Используй переменные четкие чтобы все было понятно
3 lesson
cousre_name="Python Programming" # нельзя так писать но pep8 Исправит всё
_________________________
4 less
course = "Python Programming" № можно и одинарные
message = """  # когда так пишем
Hi john,
blalbla
"""
Функция кусок кода который можно ииспользовать еще раз
course = "Python Programming"
print(len(course))    # Функция которая посчитает длинну
18 

course = "Python Programming"
print(len(course))  # 18
print(course[0])  # P
print(course[-1])  # g
print(course[0:3])  # Pyt ### будет выводить с индексом 0 1 2, поэтому Pyt 
print(course[0:])  # Python Programming c первой до последней
print(course[:3])  # Pyt также будет
print(course[:]) # Python Programming

for x in range(5): # x
    for y in range(3):  # y
        print(f"({x}, {y})")

(0, 0)      # помни сначало от 0 до 4 (range (5)) # потому что отсчет от от 0?
(0, 1)        # помни сначало от 0 до 2 (range (3))
(0, 2)     #идет сначало 0 (и так до 4(5 не входит)) прогоняется до 2 (3 не входит в это число)
(1, 0)    # потом идет 1 прогоняется до 2 (3 не входит) и так до 4 (5 не входит)
(1, 1)
(1, 2)
(2, 0)
(2, 1)
(2, 2)
(3, 0)
(3, 1)
(3, 2)
(4, 0)
(4, 1)
(4, 2)


_______________________________________________________
4.1 less
# \"    будет видна только Python "Programming
# \'  Python 'Programming
# \\   Одна палочка будет Python \Programming
# \n new line новая строка Python
# Programming

course = "Python \nProgramming"
print(course)

first = "Mosh"
last = "Hamedani"
full = first + " " + last 
print(full) # Mosh Hamedani


first = "Mosh"
last = "Hamedani"
full = f"{first} {last}" # но так лучше главное чтобы отступов с f не было будет между переменными
print(full)  # Mosh Hamedani

first = "Mosh"
last = "Hamedani"
full = f"{len(first)} {last}" # Mosh 4 Буквы
print(full) #  4 Hamedani

first = "Mosh"
last = "Hamedani"
full = f"{len(first)} {2 + 2}"    # 4 4
print(full)  # 4 4
_________________________________
6 Less
course = "Python Programming"
course. # и вижу разные функции методы объекты имеют функции называем методами


course = "Python Programming"
print(course.upper())    
# PYTHON PROGRAMMING

course = "Python Programming"
print(course.upper()) #PYTHON PROGRAMMING
print(course.lower()) # python programming
print(course.title()) # Python Programming заглавная

course = "     Python Programming"
print(course.strip()) # удобно при вводе данных пользователя
Python Programming #уберет отсутпы
print(course.rstrip())  # справо уберет отступы
print(course.lstrip()) # слева уберет отступы
print(course.replace("P", "J")) # Jython Jrogramming
print("Pro" in course)    # True
print("swift" not in course) # True

course = "  Python Programming"
print(course.find("Pro"))    # 9 Индекс укажет так P(большое) начинается с 9 в начале два отступа
_______________________________________
7 less


print(10 + 3) # 13
print(10 - 3) # 7
print(10 * 3) # 30
print(10 / 3) # 3.33333
print(10 // 3) # 3  без точки
print(10 % 3)    #  10 - 9 = 1
print(10 ** 3)  # 1000 10 в 3 степени
x = 10
x = x + 3  # равно что снизу
x += 3 # равно что сверху

print(round(2.9)) # 3 округлит
print(abs(-2.9))  # 2.9 

import math  math  #это обЪект
math.      # смотрим все функции или методы которые доступны данному объекту

print(math.ceil(2.2)) # 3 будет три

python 3 math module в yandex.ru пишешь
https://docs.python.org/3/library/math.html  # Здесь смотрим все функции и свойства

____________________________________
9 less 

x = input("x:")
print(type(x))
x:1   # выдаст <class 'str'>  укажет тип строка

x = input("x:")
y = int(x) + 1
print(f"x: {x}, y: {y}") # введу 3
# x:3
x: 3, y: 4


#y = x + 1
# будет ошибка так как "1" + 1

# int(x)
# float(x)
# bool(x)
# str(x)

# False
# ""  false но "false"  это True
# 0     false
# None
_________________________________________
10 QUIZ

fruit = "Apple"
print(fruit[1])   # A это ноль p 1
p # выведит

print(fruit[1:-1]) # A это ноль, e это -1
ppl # То что выведит e  -1 его не выведит

print(bool("false"))  # выведит true так это не пустое значение
true
___________________________________________
11

10 > 3 # true
10 == "10" # false
10 != "10"  # true
"bag" > "apple" true 
"bag" == "BAG"  false
___________________________________________
13
temperature = 35
if temperature > 30:
    print("It's warm")
    print("Drink water")
print("Done")
It's warm     # выведит так  35 > 30
Drink water
Done

temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")    #смотри обязательно отступы
print("Done")
Done # вывод так как 15 меньше


if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
print("Done")
It's nice
Done

temperature = 15
if temperature > 30:  # если это не true
    print("It's warm")
    print("Drink water")
elif temperature > 20:  # если это не true
    print("It's nice")
else:            # Тогда
    print("It's cold")
print("Done")
It's cold
Done
_______________________________________________________________________________-

14

age = 22
if age >= 18:
    print("Eligible")  # подходящий
else:
    print("Not eligible")


age = 22
if age >= 18:
    message = ("Eligible")  # message
else:
    message = ("Not eligible") # message типо улучшили код
print(message)



age = 22
message = "Eligible" if age >= 18 else "Not eigible" # будет  Eligible если age меньше либо равно 18 иначе Not Eligible
print(message)
___________________________________________________________________________
15 Operators
and
or
not
__________________________
high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligble") #Eligble
___________________________
high_income = False #!!!
good_credit = True

if high_income and good_credit: # так как один из них false
    print("Eligble")
else:
    print("Not eligible") #Not eligible
_____________________________

high_income = False
good_credit = True

if high_income or good_credit:
    print("Eligble")
else:
    print("Not eligible") # Ответ будет Eligble 
________________
student = True
if not student:        # условие что студент false а у нас student = True выведит Not eligble    
    print("Eligible")
else:
    print("Not eligble")
Not eligble        


student = False
if not student:        # false и там и там выведит Eligble    
    print("Eligible")
else:
    print("Not eligble")
Eligble
_________________
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:  # здесь мы указываем три условия или high или good одно из них выполняется true и and not student что значит false значит все выполняется выведи true
    print("Eligble")
else:
    print("Not eligible")  # Ответ будет Eligble
___________________________________________________________________________________

16
high_income = False
good_credit = True
student = True

if high_income and good_credit and not student:  # ему надо чтобы было True везде и он сразу видит False заканчивает свою работу
    print("Eligble")
______________________________________
high_income = False
good_credit = True
student = True

if high_income or good_credit or not student:  # интепретатор смотрит false но он надеятся на True слудующие True он остаавливается  и ничего не выводит
   print("Eligble") 

__________________________________________________________________________________  
# age should be between 18 and 65
age = 22
if age >= 18 and age < 65:
    print("Eligible")

# age should be between 18 and 65 
age = 22            # так сокращенно
if 18 <= age < 65:
    print("Eligible")
_________________________________________________________________________________
less 17

if 10 == "10":  # False число не равно строке!!!!
    print("a")
elif "bag" > "apple" and "bag" > "cat": # false одно из них не выполняется
    print("b")
else:
    print("c")  # ответ с
с
_________________________________________________________________________________________
for number in range(3):  # печатаю три раза что-то 
    print("Attempt")
Attempt
Attempt
Attempt
=------------------------------------------------------------
for number in range(3):
    print("Attempt", number)
Attempt 0
Attempt 1
Attempt 2
-----------------------------------------------------
for number in range(3):
     print("Attempt", number + 1)
Attempt 1
Attempt 2
Attempt 3
---------------------------------------------------------------------
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")
Attempt 1 .
Attempt 2 ..
Attempt 3 ...
-----------------------------------------------------------------------------------------
for number in range(1, 4): # до 4 мы не доходим
    print("Attempt", number, number * ".")
Attempt 1 .
Attempt 2 ..
Attempt 3 ...
--------------------------------------------------------------------------------------------

for number in range(1, 10, 2):  # 2 это степ получает 1 потом 3 потом 5 потом 7 потом 9
    print("Attempt", number, number * ".")
Attempt 1 .
Attempt 3 ...
Attempt 5 .....
Attempt 7 .......
Attempt 9 .........
-------------------------------------------------------------------------------
for else 19

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Succesful")
        break
Attempt
Succesful
---------------------------------------------------------------------------------
successful = True # ключевой момента
for number in range(3):
    print("Attempt")
    if successful:
        print("Succesful") #тут будет true Тоже
        break
else:
    print("Attempted 3 times amd failed")
Attempt
Succesful
----------------------------------------------------------------------------------------------

successful = False # Fal
for number in range(3):
    print("Attempt")
    if successful:
        print("Succesful")
        break
else:
    print("Attempted 3 times amd failed")

Attempt
Attempt
Attempt
Attempted 3 times amd failed
-----------------------------------------------------------------------------------------------------
for x in range(5): # x
    for y in range(3):  # y
        print(f"({x}, {y})")

(0, 0)      # помни сначало от 0 до 4 (range (5)) # потому что отсчет от от 0?
(0, 1)        # помни сначало от 0 до 2 (range (3))
(0, 2)     #идет сначало 0 (и так до 4(5 не входит)) прогоняется до 2 (3 не входит в это число)
(1, 0)    # потом идет 1 прогоняется до 2 (3 не входит) и так до 4 (5 не входит)
(1, 1)
(1, 2)
(2, 0)
(2, 1)
(2, 2)
(3, 0)
(3, 1)
(3, 2)
(4, 0)
(4, 1)
(4, 2)
---------------------------------------------------------------------------------------------------
11 iterables
print(type(5))
print(type(range(5)))
<class 'int'>
<class 'range'>
----------------------------------------------------------------------------------
for x in range(5):
    print(x)
0
1
2
3
4
---------------------------------------------------------------------
for x in "Python":
    print(x)
P
y
t
h
o
n
---------------------------------------------------------------------
for x in [1, 2, 3, 4]: # прогоним лист по его объектам
    print(x)
1
2
3
4
---------------------------------------------------------------------------------

number = 100
while number > 0:
    print(number)
    number //= 2  # просто дели на 2
100
50
25
12
6
3
1
----------------------------------------------------------------------------------
command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command) # даю несколько параметров

>2 + 2 # ввожу 2+ 2
ECHO 2 + 2 # ответ
>quit  # выйти
ECHO quit # но если написать QUIT не сработает
----------------------------------------------------------------------------------
command = ""
while command != "quit" and command != "QUIT": # пока любая команда не равна команде QUIT или quit
    command = input(">")
    print("ECHO", command) # даю несколько параметров

>2 + 2 # ввожу 2+ 2
ECHO 2 + 2 # ответ
>quit  # выйти
ECHO quit # ----------------------------------------------------------------------------------
command = ""
while command.lower != "quit": # пока любая команда не равна команде QUIT или quit
    command = input(">")
    print("ECHO", command) # даю несколько параметров

-------------------------------------------------------------------------------
command = ""
while command.lower != "quit":  # делаем lower чтобы писало с маленькой буквы как бы пользователь данные
    command = input(">")
    print("ECHO", command)  # даю несколько параметров
----------------------------------------------------------------------------

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print({f"We have {count} even numbers"})

PS C:\HelloWorld> python app.py
2
4
6
8
{'We have 4 even numbers'}