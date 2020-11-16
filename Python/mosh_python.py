Mosh
Siamion
sam3030034
Id 31202678



до 3: 55 основа по python

django 5:00

youtube субтитры отключить включить с

crtl + j это с новой строки
shft + @ это кавычки """"
решетка shift 3 #
одинарные кавычки просто кнопка @
| shift + решетка
* shift + 8

# shift + 3
: shift + возле L
pycharm масштабирование текста view = toolbar = setings=font=
изменение переменных правой кнопкой маши refactor = rename вводишь и все
или Shift + F6

ctrl + Tab переключение между вкладками


$ shift + 4

создание новой директории = New direction=ecommerce
в ecommerce создаю новый файл __init__.py

https://docs.python.org/3/py-modindex.html
модули все в python



ctrl shift p поисковик в visual studio code
в папке открыть окно команд shift правой кнопкой мыши а там уже дописывай файл







подсказки по python
чтобы не писать a = a + b можно указать a += b
a % = b показывает остаток за запятой

import math # импотируем библиотеку
#print (math.ceil(4.3)) возврашает следуюшие целое число 5
#print(math.sqrt(25)) считаем корень

 a = 5
 b = 3
 a + b
8
 a + _ # _ дает число предыдущие присвоение к переменной
13

a, b = 0, 1
while a < 10:
    print (a)
    a, b = b, a+b

__________________________________________




first lesson


print("hello world")
print('o-----')
print('||')
print('*' * 10)# создаст 10 точек

second lesson

price = 10 #int
rating = 4.9# float
name = 'Mosh'# str
is_published = False
print(price)

full_name = 'John Smith'
age = 20
is_new = True

3 lesson
name = input('What is your name?')
print('Hi ' + name) 
программа поздоровается со мной

name = input('What is your name?')
favorite_color = input('What is your favorite color')
print(name + ' likes ' + favorite_color)
программа  определения лучшего цвета


birth_year = input('Birth year: ')
age = 2019 - int(birth_year)  # программа определяет возраст birth year перевожу в Int
print(age)

print(type(age)) # сообщает тип перерменной


weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
___________________________________________________________________________

4 lesson
course = "Python's Course for Beginners" # что бы не было ошибок из запятой
print(course)

course = 'Python for "Beginners"' # если хочешь выделить что-то в кавычки и что бы программа хорошо работала

print(course)


course = '''
Hi john,

Here is our first email to you. 

Thank you,
The support team

'''
несколько строк

course = 'Python for Beginners'
print(course[-2])
r # так как идет с конца

course = 'Python for Beginners'
print(course[0:3])
выведит pyt но h не выведит несмотря на точто он 3 индекс имеет из-за того что нумерация идет 012


course = 'Python for Beginners'
print(course[0:])

Python for Beginners


course = 'Python for Beginners'
print(course[1:])
ython for Beginners

course = 'Python for Beginners'
print(course[:5])
Pytho

course = 'Python for Beginners'
another = course[:]
print(another)

Python for Beginners

name = 'Jenifer'
print(name[1:-1])
enife# пойдет enife так как е последния это и есть -1

course = 'Python for beginners'
course = 'Python for beginners'
print(course)
print(course.upper()) # методы
print(course.lower())
print(course.find('P'))# будет ноль так как первая буква P
print(course.find('O'))# -1
course = 'Python for beginners'
print(course.replace('beginners', 'Absolute beginners')) # а тут просто добавит слово новое
print (course.replace('P', 'b')) # перерставит их местами  
print('Python ' in course) # выведит TRUE

course = 'Python for beginners'
len()
course.upper()
course.lower()
course.title()
course.find()
course.replace()
'...' in course


print(10 + 3)
print(10/3) # 3.3333
print(10//3)# 3 чисто три
print(10%3) # ответ 1 так как 3*3=9 10-9=1
print(10**3) # ответ 1000
x = 10
x = x + 3
x += 3  # одинаковая строка что и выше строко они одинаковы
x = 10 + 3 * 2 **2 # Ответ 22 сначало 2 в степени 2 потом умножаем на три потом прибавляем
x = (10 + 3) * 2 ** 2 # сначало скобки потом степень а потом уже умножение
скобки всегда первей потм степень

x = 2.9
print(round(x))
округление ответ будет 3
print(abs(-2.9)) # сделает 2.9



is_hot = True
if is_hot:
    print("It's a hot day") # двойные кавычки так как в тексте используются апостраф в скобках


is_hot = True
if is_hot:
    print("It's a hot day")
    print('Drink a water')
print("Enjoy your day") # выведит чисто как на печатано 
но если 
is_hot = False
то выведит чисто 
Enjoy your day
так как те значения false на улице не жарко

is_hot = False
if is_hot:
    print("It's a hot day")
    print('Drink a water')
else:
    print("It is a  cold day")     # выведит сначало эти строки потом последние
    print("Wear warm clothes")
print("Enjoy your day")


is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print('Drink a water')
elif is_cold:
    print("It is a  cold day")
    print("Wear warm clothes")
else:
    print("Enjoy your day")  # Выведит чисто эту строкку


has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit: # and используется когда оба True если одно из них False ничего не выведит просто
    print("Eligible for loan")

has_high_income = True
has_good_credit = False
if has_high_income or has_good_credit: # or (если или это или это) здесь все выведит  так одно из условий true но если оба False ничего не сработает
    print("Eligible for loan")


has_good_credit = True
has_criminal_record = False # если будет TRUE то тогда функция не выведится

if has_good_credit and not has_criminal_record: # not если изначально false То прога посчитает это как True но если изначально True  то тогда ничего не выведит
    print("Eligible for loan")


temperature = 35

if temperature > 30: # == равно ,  => <=, != НЕ РАВНО
    print("It's a hot day")
else:
    print("It's a not hot day")

————————————-
Админка авторизация 
name = "J"
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a a maximum of 50 characters")
else:
    print("Name looks good!")


weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
   converted = weight * 0.45
   print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")


i = 1
while i <= 5:
    print(i)
    i += 1   # чтобы цикл не был бесконечным
print("Done")




i = 1
while i <= 5:
    print('*' * i) # помни про кавычки
    i += 1
print("Done")
*
**
***
****
***** # то что будет выводить


command = input ("> ").lower() № сразу понижаем ввод мелкими буквами

while True: # пока выполняется и является истиной


for item in 'Python':
        print(item)
   

P
y
t
h
o
n

for item in ['Mosh', 'John', 'Sarah']:
        print(item)

Mosh
John
Sarah


for item in range(10): #range функция
    print(item)
0
1
2
3
4
5
6
7
8
9

for item in range(5, 10):
    print(item)

5
6
7
8
9

for item in range(5, 10, 2):
    print(item)

5 # разница с предудущим в том что на 2 следующие число больше
7
9


for x in range(4):
    print(x)
0
1
2
3

for x in range(4):
    for y in range(3):
         print (f'({x}, {y})')

C:\Users\nicer\PycharmProjects\HelloWorld\venv\Scripts\python.exe C:/Users/nicer/PycharmProjects/HelloWorld/app.py
(0, 0) # просто прогонт от 0-3(4) с от 0-2(3)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
(2, 0)
(2, 1)
(2, 2)
(3, 0)
(3, 1)
(3, 2)


numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)

xxxxx
xx
xxxxx
xx
xx

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
            output += 'x'
            print(output)

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names [0])

John

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names [-1])
Mary


names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names [2:])
['Mosh', 'Sarah', 'Mary']

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names [2:4])
['Mosh', 'Sarah'] # мы увидим двойку Mosh Sarah но 4 последнию позицию мы не увидим
_______________________________________

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names [2:]) # НО ПОМНИ ДАННАЯ КОМАНДА ВЫВЕДИТ ВСЕ ДО КОНЦА НАЧИНАЯ С 2 НОМЕРА

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names [:])
['John', 'Bob', 'Mosh', 'Sarah', 'Mary']


names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names [2:])
print(names)

['Mosh', 'Sarah', 'Mary']
['John', 'Bob', 'Mosh', 'Sarah', 'Mary'] # новый лист создается

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Jon'
print(names) # изменение списка
['Jon', 'Bob', 'Mosh', 'Sarah', 'Mary']


numbers = [3, 6, 2, 8, 4, 10]
max = numbers [0]
for number in numbers:  # обрати вниманию на эту строку поиск а данной строке
    if number > max:
        max = number
print(max)

________________

numbers = [5, 2, 1, 7, 4]
numbers.append(20) #добавил номер 20 в конец лист
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers.insert(0, 10)
print(numbers)
[10, 5, 2, 1, 7, 4] # добавил 10 как самую первую

numbers = [5, 2, 1, 7, 4]
numbers.remove(5)
print(numbers)
[2, 1, 7, 4] # убрал 5

numbers = [5, 2, 1, 7, 4]
numbers.clear() # просто ощищает лист полностью () в скобках ничего не указывай
print(numbers)
[] 


numbers = [5, 2, 1, 7, 4]
numbers.pop() # просто последнию цифру удаляю в списке
print(numbers)
[5, 2, 1, 7] 

numbers = [5, 2, 1, 7, 4]
print(numbers.index(5)) # я узнаю index числа 5 он является 0 так как это первая цифра
 0


numbers = [5, 2, 1, 7, 4]
print(50 in numbers) # проверка есть ли 50 в списке
False # если есть это число то напишет True

numbers = [5, 2, 1, 5, 7, 4]
print(numbers.count(5))
2 # посчитает количество 5 в списке в данном примере их две

numbers = [5, 2, 1, 5, 7, 4]
numbers.sort()
print(numbers)
[1, 2, 4, 5, 5, 7] # просто отсортирует по списку


numbers = [5, 2, 1, 5, 7, 4]
numbers.reverse()
print(numbers)
[4, 7, 5, 1, 2, 5] # просто прогонит задом нанаперед

numbers = [5, 2, 1, 5, 7, 4]
numbers.sort()
numbers.reverse()
print(numbers)
[7, 5, 5, 4, 2, 1] # сначало отсортирует от 1-7 , а потом сделает задом на перед


numbers = [5, 2, 1, 5, 7, 4]
numbers2 = numbers.copy() #скопировал первый лист и присвоил его numbers2
numbers.append(10) #добавил в первый лист 10
print(numbers2)
[5, 2, 1, 5, 7, 4] # но выведит только первый лист так как изначально я делал его копию

numbers = [2, 2, 4, 6, 3, 4, 6, 2]
uniques = [] # дублирую список 
for number in numbers: # создаю number (в numbers)
    if number not in uniques: # если нету number добавить в unique number 
        uniques.append(number)
print(uniques)
[2, 4, 6, 3]

numbers = (1, 2, 3) # Это кортеж он неизменяем его тяжело изменить
numbers[0] = 10 # не сработает появиться ошибка
print(numbers[0])



coordinates = (1, 2, 3)
x = coordinates[0]
у = coordinates[1]
z = coordinates[2]

x, y, z, = coordinates   # эти строки с переменными будут одинаковыми что вверху что внизу
оно просто поочередно присвоет каждому по числу по порядку unpacking называется

coordinates = (1, 2, 3) # кортеж эта круглая скобка
x, y, z, = coordinates
print(x) 
1 # Напечатает

coordinates = [1, 2, 3]
x, y, z, = coordinates
print(y)
2  # также и со списком



СЛОВАРИ

customer = {  #  после названия словаря равно и такая скобка для словарей каждое ключевое слово в словаре не можт быть два Name дублироваться используется к примеру как информация о наших покупателях к примеру почто, адрес  и т.д.
    "name": "John Smith", # словарь называется customer туда ложим какие-то данные 
    "age": 30,
    "is_verified": True
}
print(customer["name"]) # но если ввести blabla то будет ошибка
John Smith
Ключь и слово как словарь английский и русский 

print(customer.get("name"))
John Smith

print(customer.get("blalba"))
None # вместо ошибки выведит none

print(customer.get("birthdate", "Jan 1 1980"))
Jan 1 1980 #добавит новое слово в словарь и выведит его свойство


customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["name"] = "Jack Smith" # добавил новое значение name
print(customer["name"])

customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])  # мы просто добавили новое слово в наш словарь
Jan 1 1980

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " " # здесь мы будем указывать get так как если пользователь введет чтл-то нето просто выедит ему !!!!!!!
print(output)

Функции

def greet_user():
    print('Hi there!')
    print('Welcome aboard')

greet_user() # создал функцию и вызвал ее!!!

Hi there!
Welcome aboard


def greet_user():
    print('Hi there!')
    print('Welcome aboard') # не печатает так они находятся в функции чтобы распечатало ее надо вызвать

        # обязательно два отступа после функции
print("Start") 
greet_user()
print("Finish")

Start # сначало печатает start потом функцию
Hi there!
Welcome aboard
Finish


greet_user () # не сработает будет ошибка

def greet_user():
    print('Hi there!')
    print('Welcome aboard')




def greet_user(name):  # очень удобно указал name
    print(f'Hi {name}!') # также и я могу водить одни и те же имена и мне не надо плодить код цепь кода остаются одна
    print('Welcome aboard')

print("Start")
greet_user("John")
greet_user("Mary")
print("Finish")

Start
Hi John!
Welcome aboard
Hi Mary!
Welcome aboard
Finish


def greet_user(first_name, last_name): # параметры
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

print("Start")
greet_user("John", "Smith") # это аргументы, их можно переставлять местами 
print("Finish")

Start
Hi John Smith! # просто выводит Имя с фамилией
Welcome aboard
Finish

print("Start")
greet_user("Smith","John")
print("Finish")
Start
Hi Smith John! # !!!!!! просто поменяет местами
Welcome aboard
Finish

print("Start")
greet_user(last_name="Smith", first_name="John") # тут я поменял местами но присвоил класс поэтому сработало как указано в функции
print("Finish")

Start
Hi John Smith!
Welcome aboard
Finish

def square(number):
    return number * number


result = square(3)
print(result) # выведит 9


def square(number):
    return number * number


print(square(3)) # так код просто короче

def square(number):
    print(number * number)


print(square(3))

9 # Выведит 9 но потом None потому что нету return
None


age = int(input('Age: ')) #int перед input строку Age превращаю в цифровую строку
print(age)
3

Process finished with exit code 1 # в python имеется ввиду программа crushed
Process finished with exit code 0 # имеется ввиду все нормально

age = int(input('Age: '))
    print(age)            #если я ввиду sd произойжет ошибка

ValueError: invalid literal for int() with base 10: 



try:
    age = int(input('Age: '))
    print(age)                   #Здесь пользователю предлагается попробовать вести данные, но если он указывает текст то ошибка 
except ValueError:        #except ValueError не учитвается если пользователь захочет ввести строку вместо цифр
    print('Invalid value')

Age: вфывфв # к примеру  ввел строку мне выскочет такое сообщение 
Invalid value

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:  #это для того чтобы исключить ошибку с указанием 0 смотри внизу терминала на тип ошибки
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')

# коментов должно быть поменьше и только там где это нужно



Классы
class Point:       # я создаю класс и присваиваю ему функции
    def move(self): # body of class
        print("move")

    def draw (self):
        print("draw")


point1 = Point() # Здесь я переменной присваиваю класс
point1.draw() # ввожу переменную нажав . мне сразу выскакивают подсказки функций которые принадлежат данному классу
draw             


class Person:
    def talk (self):
        print("talk")


john = Person()
john.talk()
talk


    def __int__(self, name): # конструктор


class Person:       # создал класс
    def talk(self):  # присвоил ему функцию
        print("talk")

john = Person()       # john присвоил клас
john.talk()          # john присвоил одну из функций класса




РОДИТЕЛИ
class Mammal:            #  создаю класс родитель с его функцией
    def walk(self):    
        print("walk")            


class Dog(Mammal):     # создаю дочерний класс и указываю его родителя
    pass        #python не парься (не любит пустые классы)


class Cat(Mammal):
    pass

dog1 = Dog()      # создаю объект c классом dog
dog1.walk()         #запускаю функцию родителя метод называется



class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self): # создаю новую функцию
        print("bark")


class Cat(Mammal):
    def be_annoying(self): # создаю новую функцию
        print("annoing")

dog1 = Dog()
dog1.bark()     # когда ставлю . выскакивает подсказка двух методов родительского класса и класса дочернего внутри которого создана новая функция

cat1 = Cat()
cat1.be_annoying()



Чтобы не плодить кучу нового кода и часто не вводить новые функции

создаем новый файл нажимаю project1=new=converters.py

converters.py туда запрасываю функции:
def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45

Захожу в файл app.py
import converters # просто без .py

print(converters.lbs_to_kg(70))
155.55555555555554


from converters import kg_to_lbs # импортиовать можно конкретную функцию
.converters #вызов функции или метода

kg_to_lbs(100)


import utils      # можно так импортировать
utils.find_max()

from utils import find_max




def calc_shipping():
    print("calc_shipping")

import ecommerce.shipping

ecommerce.shipping.calc_shipping() # ecommerce директория shipping это название самого файла

from ecommerce.shipping import  calc_shipping # тоже самое только вверху прописываешь путь и конкретную функцию

calc_shipping() # вызов ее

import openpyxl as xl открываем работу с excel 

