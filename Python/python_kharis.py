0  ModuleNotFoundError: No module named 'lxml # решение ошибки 
1 python3 -m venv venv # в папке проекта
2 source venv/bin/activate # активировал 
3 pip install lxml
4 pip install requests



1 python3 # вызов REPL в консоли
2 python3 hello.py # запуск приложения
3 python3 -m idlelib.idle # открываю idle где можно создавать сохранять файлы и запускать их f5 запуск

4 1 #!/usr/bin/env python3              
""" путь к питону """
    print("Hello world")
  2 chmod +x hello.py # даю права на исполнение
  ./hello.py # запуск приложения

5.1 Справка 
python3 # справка по модулю в терминале ввожу
help()
help> keyword

6 >>> import keyword # узнаю про ключевые слова нельзя использовать как переменные
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 

7 dir(__builtins__) # узнать встроенные имена которые негодятся для переменных
===========================================================================
Глава ввод(int) вывод(print) данных


Вывод данных(print)
1 print("hello there")
hello there
2 >>> print("I'm", 10, 'years old') # обрати внимание здесь ввод строк и чисел 
I'm 10 years old     # запятые не видны они работаю как запятые

Ввод данных user(input)
1 name = input("Enter your name: ") 
""" пользователь вводит данные мы сохраняем в name а потом крутим вертим эту переменную name """
print(name)
 """переменная просто вводим название без кавычек что делаю с name"""

2 input всегда возвращаест строку

>>> value = input('Enter a number:')
Enter a number:2

>>> other = input('Enter another:' )
Enter another:3

>>> value + other
'23' ## неожиданный результат так как мы сложии строки а не числа
>>> type(value)
<class 'str'> ## говорит что тип строка

int(value) + int(other)
""" Превращаю строки в числа и складываю их"""
5 # вывод 2 + 3

6 Задание 
"""Запросить имя и поздороваться """
1 name = input("Enter your name: ") 
print('Hello', name)
Hello sam #вывод

2 ''' Запросить сколько лет и сказать сколько будет в следующем годуы '''
age = input('Enter your age: ')
next_age = int(age) + 1
print("Your age next year", next_age)


Итого:
вывод print , ввод input
====================================================================================
Глава ПЕРЕМЕННАЯ 
Состояние, изменение
Программирование можно с моделировать все.
Лапмочка может обладать состояением, вкл, выкл, яроксть_max, яркость_min, переход из одного состояния в другое 
это изменение. Ламочка(объект) которая обладает теми или иными свойствами(состояниями).

1 Переменные как метки
переменные используется для хранения состояния

status = "off" ## запоминаю состояние лампочки
""" переменная status "off" это строковый тип данных""" 

2 Когда выхожу из конкретной функции переменные этой функции исчезают. Когда объект никому не нужен, счетчик равен 0 его 
подвергают уборке мусора. Если на объект указывают переменные или другие объекты то счетчик положителен и все норм.
>>> import sys
>>> names = []
>>> sys.getrefcount(names)
2
""" Узнаю счетчик ссылок"""

3 Информация о людях состояния:
'''Бирка на корове это грубо говоря как переменная '''
имя 
возвращаест 
адрес

4 status = 'off'
print(status)
""" мы создали переменную status позже когда нам надо узнать ее значение мы обратимся к ней как выше """
'''У объекта есть значение "off", тип строка, индетификатор(местонахождение в памяти как пример id(a) )
создается переменная и связывается с ней '''

5 "120 watt" ## мы создали строковый объект но теперь не можем к нему обратиться

wattage = "120 watt" 
''' теперь можем обратиться по переменной это одно из состояний лампочки '''
incandescent = wattage
wattage = "25 watt"
print(incandescent, wattage)
120 watt 25 watt
''' обрати на вывод сначало 120, а потом уже то что мы поменяли '''

6 Повторное связывание переменных
num = 400
num = '400' 
''' теперь это строка то что выше num = 400 уборщик мусора уничтожит '''
''' переназначение переменных не лучшая практика запутывает '''

7 Нельзя называть переменную по ключевому слову
"""Узнать все ключевые слова """
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 

8 Имена переменных
1 переменная нижнего регистра
2 можно использовать _
3 нельзя чтобы начинались с цифр
4 имена переменных не могут переопределять встроенные функции

Пример:
goog = 4 # +
bAd = 5 # верхний регистр -
a_longer_variable = 6 # +

baD_Longer_Var = 7 # так не очень
3treepy = 5 # так нельзя начало с цифр
for = 4 # нельзя ключевое слово
compile = 4 #нельзя встроенная функция

9 Встроенные имена которые нельзя использовать
dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError',
 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 
 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
  'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError',
   'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 
   'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 
   'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 
   'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 
   'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 
   'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError',
    'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', 
    '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__',
     'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 
     'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate',
      'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 
      'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list',
       'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
        'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str',
         'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> 
===============================================================================
Объекты:
1 индетификатор
2 тип
3 значение  

1 Индетифкитор
Определяет местонахождения в памяти компьютера
name = "Matt"
first = name
id(name)
140699256961456 # место хранения в памяти
id(first)
140699256961456 # будет один и тот же индетификатор

 Индетифкитор позволяет узнать время создания объекта и возможно ли их изменения
first is name
''' Узнаем указывают ли две переменные на один и тот же объект '''
True 
Две переменные указывают на один и тот же объект
name = "Matt"
first = name
name = 'Fred'

>>> id(name)
140699254219184 # изменился
>>>id(first)
140699256961456 # остался тот же 


2 ТИП объекта
1 строки
2 целые числа
3 числа с плавающей точкой
4 логические значения

Тип объекта это класс объекта, класс опеределяет состояние данных хранящихся в объекте, также методы(действия),
которые может выполнить объект
>>>type(name) # узнаем тип объекта
<class 'str'>

Объект                    Тип

Строка                    str
Целое число               int
Число с плавающей точкой  float
Список                    list
Словарь                   dict
Кортеж                    tuple
Функция                   function
Класс с определяемый пользователем type 
Экземляр класса           class 
Встроенные функция        builtin_function_or_method
type                      type 

Для того чтобы узнать относится ли объект к типу поддерживающему некоторую операцию можно использовать встроенные классы
str , int , float , list , dict и tuple

>>> str(0)
'0' # вижу сразу строку можно ли сделать строку из этого
>>> tuple([1,2])
(1, 2)
>>> list('abc')
['a', 'b', 'c']
====================
Изменяемость 
Словари списки изменяемы
Строки кортежи целые числа, числа с плавающей точкой неизменяемые типы
Пример
1
>>> age = 1000
>>> id(age)
140532846920080 ## индетификатор

>>> age = age + 1
>>> id(age)
140532846920016 # индетификатор новый уже

2 >>> names = [] # список
>>> id(names)
140532846969280

>>> names.append('Fred') # добавил значение 
>>> names
['Fred'] 
140532846969280 # старый  id значение
140532846969280
ый id значение

Пример 3 
name = "Matt"
first = name
age = 1000
print(id(age))
age = age + 1
print(id(age))
names = []
print(id(names))
names.appent['fred']
print(id(names))


Вывод 
139756435201008 # вижу id 
139756434595536
139756435022784
139756435022784



1 python3 -m idlelib.idle
файл создать сохрани этот код = f5 
dir() # тут увижу переменные names, name
name
"Matt"
names
['Fred']


Упражнения 61 страница
1 
numb = 25
id(numb)
print(id(numb))
# 94475134881856

numb = 25 + 20
id(numb)
print(id(numb))
# 94630171501248 # разные номера

2 age = []
#id(age)
#print(id(age))
#140030905938944

age.append(300)
id(age)
print(id(age))
#140386085933952

===================================
Числа

>>> type(2)
<class 'int'>
>>> type(2.0)
<class 'float'>
У чисел с плавающей точкой есть погрешность небольшая из-за округления

Сложение 

1
>>> 2 + 6
8
>>> result = _
>>> result
8
""" так как здесь нету переменной то результат сохраняется в _ присваиваем значение переменной result """

2 >>> .4 + .01
0.41000000000000003

3 
>>> 6 +.2
6.2 # если целое число плюс с плавающей точкой то будет число с плавающей точкой 

4 print('num: %s' % 2)
num: 2

5 
>>> "Python" * 3
'PythonPythonPython' # просто сделают одну строку с тремя зачениями

>>> '4' * 2 
'44' # просто 2 раза по 4 # одна строка 2 значениями по 4 

6 Преобразования
>>> int(2.6)
2
>>> float(3)
3.0

7 Вычитание 
>>> .25 - .2
0.04999999999999999
>>> 2 - 6 
-4
>>> 6 - .2
5.8
>>> 

8 Умножение 
>>> 6 * 2
12
>>> .25 * 12
3.0


Деление 
1 >>> 12 / 4
3.0

2 >>> 3 / 4
0.75

3 >>> 3 // 4 # целочисленное деление
0

Остаток 
(Деление по модулю, находим остаток)

1 
4 % 3
1 # 4 -3 = 1 нечетное число

2 
>>> 3 % 2 
1 # нечетно если результат равен 1 

3 
>>> 4 % 2 
0 # четное число если равен 0 

4 
>>> 3 % 3
0
>>> 2 % 3
2
>>> 1 % 3
1
>>> 0 % 3
0

5 
>>> -1 % 3
2
>>> -1 % -3
-1
>>> 1 % -3
-2
>>>  
""" Но лучше так не делать """


Возведение в степень
1 
>>> 4 ** 2 # 4 в стемени 
16

2
 >>> 10 ** 100 #  10  в степени 100

3 
>>> import operator # для математических операций
>>> operator.add(2, 4)  # the same as 2 + 4 
6

Порядок операций

>>> 3 + 2 * 3
9
>>> (3 + 2) * 3
15

=====================================
Строки
неизменяемые объекты для хранения символьных данных
символ,слово, последовательность слов, абзац, несколько абзацев.
'some text' # строки заключаются ммежду символами
"some text"
""" some text """
''' some text '''

1 '''Кавычки начинаются и завешаются одним и тем же видом'''
character = 'a' 
name = 'Matt'
with_quote = "I ain't gonna"
longer = """This string has
multiple lines"""
latin = '''lorum ipsum dolor'''
escaped = 'I ain\'t gonna'  # \ если надо экранировать ковычку то делаем так как в примере
zero_chars = ''
unicode_snake = "I love \N{SNAKE}" ### будет змейка

2 
>>> backlash = '\\' # чтобы вывести \\
>>> print(backlash)
\     

3 Экранирующая последовательность
\\ Обратная косая черта
\' одинарная кавычка
\" двойная кавычка 
\b символ backspace
\n новая строка
\t табуляция
\u12af 16-разрядный символ Юникода
\U12af89bc 32-разрядный символ Юникода
\N{SNAKE} Символ Юникода
\o84 Символ в восьмеричной кодировке
\xFF Шестнадцатеричный символ

3.1 Необработанный строки тогда r
>>> slash_t = r'\tText \\'
>>> print(slash_t)
\tText \\         # благодаря r сохранится значения текста

>>> normal = '\tText \\'
>>> print(normal)
        Text \ # без r как будет отображаться

3.2 Тройные кавычки 
Нужны для строк разделенных на абзацы часто используются в строках документации
>>>
paragraph = """Lorem ipsum dolor            
sit amet, consectetur adipisicing
elit, sed do eiusmod tempor incidid """
В коде """ some comments .... """

3.3 Также внутри тройных кавычках можно использовать другие каычки и их не надо экранировать
""" this string has double " and single quotes ' inside of it """



Форматирование строк 

1 
>>> name = "Matt"
>>> print('Hello {}'.format(name)) # {} в скобках .format(name) указываю что в эти скобки {} воткнуть 
Hello Matt

2 >>> print('I:{} R:{} S:{}'.format(1, 2.5, 'foo')) # :{} в скобках format(1, 2.5, 'foo') указываю последовательность 
I:1 R:2.5 S:foo

Синтакстис форматных строк
1 >>> 'Name: {}'.format('Paul')
'Name: Paul'    # вставим имя

2 'Name: {name}'.format(name = 'Paul') #  обрати внимание {name} и название переменной name
'Name: Paul'

3 >>> 'Name: {[name]}'.format({'name' : 'Paul'}) # обрати {[name]} тут как словарь  {'name' : 'Paul'}
'Name: Paul'

4 >>> 'last: {2} First: {0}'.format('Paul', 'George', 'John') # 'Paul', 'George', 'John' это 0 1 2 
'last: John First: Paul'
''' 2 это позиция элемента  John ''' 


5 Примеры форматирования 

>>> "Name: {:*^12}".format("Ringo")
'Name: ***Ringo****'
''' * символ заполнитель, ^ поле вырвнивания, 12 поле ширины (***Ringo****)''' 


6 Справка по форматированию
>>> help()
help> FORMATTING

https://pyformat.info/



7 F -строки с python 3.6
1 
>>> name = "matt"
>>> f'My name is {name}' # указываю куда воткнуть переменную name
'My name is matt'

2 
>>> f'My name is {name.capitalize()}'
'My name is Matt'

3 
>>> f'Square root of two: {2**.5:5.3f}'
'Square root of two: 1.414' 

====================================================================
dir, help, pdb 

Функция dir возвращает атрибуты обеъекта
1 dir("Matt")  # сразу вижу все атрибуты объекта строки  видит что строка

2 Первые записи _ можно не обращать
методы(атрибуты) функции связанные с объектом

1
 >>> print("matt".capitalize())
'''c большой буквы помни про upper метод '''
Matt   
 
2 
>>> print('Hi {}'.format('there')) # {} воткнул туда при помощи .format('there') "there"
Hi there

3 
print('YIKES'.lower()) 
yikes # с малнеькой

4 при использовании использовании + или % к строке будет вызван метод __add__ или __mod__

Функция help документация метода модуля класса или функции

'''Узнаю что делает функция upper '''
help('some string'.upper)
# без интернета могу все равно читать документацию

pdb
import pdb; pdb.set_trace() # вхожу в отладчик  типо как в C gdb

h, help # вывести список доступных команд
n, next # выполнить следующую строку
c, cont, continue  продолжать выделение до следующей точки прерывания
w, where,bt ## вывести трассировку стека информацией о текущей позиции выполнения
u, up # подняться на уровень выше
d, down # опуститься на уровень ниже
l, list  # вывести исходный код текущей строки


=================================================================================
Строки и методы
Существуют методы которые позволяют проводить операции с строками
text.capitalize() # делаю с большой буквы то что храниться в переменной text
Метод не меняет саму строку, строки(неизменяемы) вместо этого метод возвращает новую строку

1 
>>> name = 'matt'
>>> correct = name.capitalize()
>>> print(correct) # Matt c большой буквы 
Matt

>>> print(name) ## name при это останется такой же
matt
>>> 

2 Работа со строковым литералом
>>> print('fred'.capitalize())      # строковый литерал
Fred

3 В python все является объектами даже методы и функции
print('fred'.capitalize) # ошибки не будет просто укажет ссылку на метод который является объектом   

Замыкантя и декораторы
Есть объекты, у которых есть методы

4 
>>> (5).conjugate()
5 # компрлексное сопряжение целого числа

>>> five = 5
>>> five.conjugate() # ставлю переменную и сразу метод
5

метод Endswith # на что заканчивается  узнаю формат
1
>>> x1 = 'oct2000.xls'
>>> x1.endswith('.xls') # узнаю какого формата файл как бы задаю вопрос он такой 
True

>>> x1.endswith('.xlsx')
False

2 help(x1.endswith) # узнаю какие параметры надо указывать

S.endswith(suffix[, start[, end]]) -> bool 
'''S это переменная (x1) имя метода .endswith обязательный параметр suffix в квадаратных скобках необязательно '''

x1.endswith('Oct', 0, 3) # заканчивается endswith
''' Например, если вы хотите убедиться в том, что часть строки с 0 и до 3 символов завершается символами « Oct » '''
True

x1.startswith('Oct')
True


Метод Find

1 
>>> word = 'gratefull'
>>> word.find('ate') # 2 вернет a начинается с индекса 2 
2
>>> word.find('great') # -1 значит ничего не нашло
-1

Метод format
1 
print('name: {}, age: {}'.format('Mat', 10))
name: Mat, age: 10

2 
>>> print('name: {}, age: {}'.\    # можно и с отступом на след строку .\ экранирую
...
format('Matt', 10))
name: Matt, age: 10

3
>>> print("word". # можно и так
...find('ord'))
3.1
>>> print("word".find(    # можно и так
...'ord'))
''' Если открыта левая круглая скобка ( , вы также можете размещать аргументы в нескольких строках без \ '''

3.2
>>> print("word".\
... find('ord'))      # обязательно 4 отступа на новой строке 
1
>>> print("word".find(
... 'ord'))
1

""" Отступы мы делаем когда хотим соблюдать стандарт 80 символов одна строка """

3.3 
>>> print('{} {} {} {} {}'.format(
  '''помни про 4 таба 4 отступа '''
...       'hello',
...       'to',
...       'you',
...       'and', 
...       'you'
... ))
hello to you and you #вывод


Метод join 
>>> ', '.join(['1', '2', '3'])
'1, 2, 3'
''' Метод .join создает новую строку
из последовательности, вставляя строку между каждой парой элементов
списка '''
склеивание 

Метод lower
1
fname = 'readme.txt'
fname.endswith('txt') or fname.endswith("TXT")  ## проверка какого расширения TXT
True

2 lower но лучше так 
>>> fname.lower().endswith('txt')    # проверка на нижний регистр
True

Метод startwith  # начинается с строки проверка с большой буквы
>>> 'Book'.startswith("B")
True
>>> 'Book'.startswith("b")
False


Метод strip(раздеть)
>>> ' hello there '.strip() # убирает лишние отступы по бокам 
'hello there'               # удобно для обработки данных введенных пользователей!!!!!!
'''lstrip rstrip удаляем слева отступы и справа отступы '''


Метод upper
'yell'.upper()
'YELL'

===============================================================================================
Комментарии, логические значения none
Комментарий должен показывать почему а не как, как кода должно быть достаточно

# this is comment
num = 3,14 # PI


Логические значения True False
1 'bar'.startswith(b) # стартует с b
True

2 >>> type(True)
<class 'bool'>

3 Можно присвоить значения переменным
a = True
b = False

4 
>>> bool('')  # «квазиложным» поведением
False
>>> bool('0') # «квазиложным» поведением
True

4.1 
name = 'Paul'
if name:
        print("The name is {}".format(name))
else:
        print("Name is missing")
# The name is Paul 

4.2 Проверка ввода пользователя 

if len(name) > 0:               ## не очень хорошая практика
  print("The name is {}".format(name))


if bool(name)                   ###тоже не очень практика
  print("The name is {}".format(name))

Правильный путь !!!!!
name = input("Enter your name: ")   # сохраняю ввод пользователя в переменную 
if name:                        # python проверит значение if и преобразует его в логическое значение  
  print("The name is {}".format(name))   ### 
  The name is sam

'''int float str bool являются встроенными функциями
class str(object)
 '''  
bool(0) # 0 типо всегда false
False

bool(4) #  а тут true
True

bool("False") # True не пустая строка всегда будет True 
True 

Не проверяй на True
1 if done:    ## так будет достаточно
  .....

2 if done == True # так делать нельзя
3 Как и эта проверка

if bool(done):
  ......

3 members = []
  if members:
    # Действия 
    # содержит значения
  else:
    # список members пуст
3.1 проверка на квазиистинност списка по его длине так не правильно:
if len(members) > 0:
  # действия если members 
  # содержит значения
else:
  # список members пуст

3.2
Если вы хотите определить неявную квазиистинность для объектов, опре-
деляемых пользователем, это поведение определяется методом .__bool__ .


NONE 
1 def hello():
  print("hi")
result = hello()
print(result)
hi
None

2  У None один и тот же индетификатор
a = None
id(a)
94424215655264  ## !!! одинаковые номера

>>> b = None
>>> id(b)
94424215655264  !!!!

3 
>>> a is b  ## все что None означает что это один и тот же объект
True
>>> a is not b
False

4 
is cравнивает индетификаторы а не значения !!!!! is можно поместить в if 
a = None

if a is None:
  print("A is not set!")
  # A is not set! 

None в логическом контексте интерпретируется как False
if not a:    #интерпертируется как false
    print("A is not set!")
# A is not set!

None это одиночный объект, обозначающий переменные, значение которых должно быть присвоено
в будущем.

Грубо говоря нам нужна переменная в будущем но пока не хотим присваивать ей значение, поэтому пока none. 

=====================================================================================
Условия и отступы
логический литерал True False

1
5 > 9
False

>         Больше
<         Меньше
>=        Больше или равно
<=        Меньше или равно
!=        Не равно
is        Объекты тождественны
is not    Объекты не тождественны
Пример
a = None

if a is None: ## действительно тождественно

2 
>>> name = 'Matt'
>>> name == 'Matt'   # подтвердит что данной переменной name присвоено значение Matt 
True
>>> name != "Fred"   # подтвердит что данное значение не равно переменной name
True
>>> 1 > 3
False

3 Объединения условных выражений
x and y             выражение истинно только в том случае если истины оба операнда
x or y              выражение истинно если истинно хотя бы одно значение 
not x               логическое отрицание x (True превращается в False и наоборот)

4 
score = 91
if score > 90 and score <= 100: # можно делать такую проверку 
  grade = "A"

if 90 < score <= 100:          # могут осуществляться две проверки та что выше и эта
  grade = "A"

5
1
name = 'Paul'
beatle = False
'''Проверяем входит ли переменная name в заданную группу '''
if name == "George" or \  #\ команда продолжается с новой строки однако если писать код через () то так делать необязательно
    name == "Ringo" or \
    name == "John"  or \
    name == "Paul":
    beatle == True
else:
  beatle = False

2 
name = 'Paul'
beatle = False
if (name == 'George' or   # когда круглые скобки не нужно тогда \ как бы код продолжается дальше 
  name == 'Ringo' or
  name == 'John' or
  name == 'Paul'):
  beatle = True
else:
  beatle = False

3 Проверка наличия
name = "Paul"
beatles = {"George", "Ringo", "John", "Paul"}
beatle = name in beatles  ## переменная beatle с помощью которой узнаю есть ли Paul в словаре
print(beatle)



Команды if (True и False)
Если это условие истинно выполнить блок кода, а если нет выполнить другой код, также провяряет логические значения
debug = True
if debug:  # Проверка логического значения
  print("Debugging")
# Debugging



Команда else
Команда else может использваться в сочетании с командой if. Else выполниться только в случае если if false

score = 87 
if score >= 90:  # будет false потому что 87 меньше
    grade = "A"
else:
    grade = "B"
    print(grade)
# B     


Множественный выбор elif промежуточные шаги
sscore = 87 
if score >= 90:
    grade = "A"
elif score >= 80:    # промежуточный шаг 
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:                 # тогда
    grade = "F"
print(grade)
# B

if elif else имеет собственный блок кода
python начинает сверху вниз опускаться проходя по каждому блоку ища значение True. 
Если не найдет в if elif True пойдет тогда else:
  
В команде if может содержать ноль и более команд elif. Наличие команды else не обязательно. Но если надо то может
быть только один else в команде if !!!!!!!

if
elif
else

Пробелы

Строки следующие после команды if снабжаются отступами из 4 пробелов !!!!!!!
Пример
if:
    grade = "A"  
Эти строки и называются блоками кода который выполниться если if даст True

Другие языки программирования пример
if (score >= 90) {
  grade = "A"        
}
() {} это блоки кода и выполниться то что в {} только при условии что в () выполниться больше либо равно 90

В python вместо таких скобок используется:
1 Двоеточие  :
2 Отступы
Пример

score = 87 
if score >= 90:      ## : это одна часть блока типо как в других () python пробегается по данным блокам
    grade = "A"      ## : отступы это другая часть кода типо как {} в других языках

Согласно PEP 8, в Python рекомендуется использовать отступы из четырех пробелов.

 TabError   # ошибка связанная смешиванием пробелов и табуляции

===================================================================================
Контейнеры списки кортежи множества

Списки 
Используются для хранения списков объектов, в списках могут содержаться разные типы данных, но как правило там один тип данных
Список можно менять добавлять удалять

1 >>> list("Mat")     # создам список из строки Matt при помощи функции list
['M', 'a', 't']        # список

2  other_names = ['Fred', 'Charles']   # базовый список 

3 У списков есть свои методы
>>> names = []

>>> names.append("Fred")  # метод круглые скобки добавляем новый объект в список names в конец списка
>>> names.append("Matt")
>>> print(names)
['Fred', 'Matt']



==========

Индексы
С каждым элементов списка связан индекс, описывающий его местоположение в списке.
Первый элемент это ноль и так далее, помни нумерация начинается с 0.


>>> names         ## наш список 
['Fred', 'Matt']
>>> names[1]       # обращение к элементу по индексу
'Matt'

==========

Вставка с список
Вставка с список с определенным индексом используется метод insert

1
>>> names = ['Fred', 'Matt']
>>> names.insert(0, "Fred")     # воткнул Fred и присвоил ему индекс 0, самый первый элемент
>>> names
['Fred', 'Fred', 'Matt']

2 
names = ['Fred', 'Fred', 'Matt']
>>> names[1] = "Joe"    ## заменил Fred на Joe
>>> names
['Fred', 'Joe', 'Matt']

3 
Добавляю в конец списка при помощи:
>>>names = ['Fred', 'Joe', 'Matt']
>>> names.append("Sam")
>>> names
['Fred', 'Joe', 'Matt', 'Sam']   ## теперь Sam  в конце списка

Операции присоединения и удаления в конце списка выполняются быстро (O(1)), тогда как операции вставки и удаления
в середине списка выполняются медленнее (O(n)). Если окажется, что вам часто приходится вставлять и извлекать элементы в начале списка, лучше
использовать структуру данных collections.deque.

===================
Удаление из списка 

1 names = ['Fred', 'Fred', 'Matt']
names.remove("Fred")
print(names)
['Fred', 'Matt']

2 Удаление по индексу 
names = ['Fred', 'Matt']
del names[1]
print(names)
['Fred']

==================
Сортировка списков частая операция

1 names = ['Fred', 'Adam', 'Matt']
names.sort()
print(names)
# ['Adam', 'Fred', 'Matt'] 
''' Отсортирует текущий список не будет создавать новый, отсортирует по алфавиту '''

2 Если список нужен то в начале сксопируйте его перед сортировкой пример ниже.
Для сортировки последовательностей можно использовать sorted.

old = [5, 3, -2, 1]
nums_sorted = sorted(old) # отсортированный список сохраняю в новую переменную
print(nums_sorted) # новый отсортированнный список 
print(old)         # старый список который остался до сортировки
#[-2, 1, 3, 5]       # отсортирует в числовой последовательности
#[5, 3, -2, 1]

3 При сортировки списка с разнотипными элементами может произойти ошибка
1 
things = [2, 'abc', 'Zebra', '1']
things.sort()
# TypeError: '<' not supported between instances of 'str' and 'int'
# сортировка разных типов данных решается указанием key пример
# things.sort(key=str) то есть теперь python понимает, что сортировка происходит по правилам сортировки строк

2 Решение ошибки выше

things = [2, 'abc', 'Zebra', '1']
things.sort(key=str)
print(things)
# ['1', 2, 'Zebra', 'abc'] 

# Помните, что список сортируется «на месте». В результате вызова метода .sort список изменяется, а сам метод
# возвращает None

# Сортировка списка функцией sorted. Обратите внимание: список не изменяется, а при вызове возвращается новый список
===================
Полезные советы по работе со списками
помни про dir, help

1 range
>>> nums = range(5)
>>> nums
range(0, 5) 
''' Функция range не материализует список а возвращает числа которые будут при переборе '''

2 Однако можно использовать list
>>> nums = range(5)
>>> nums
range(0, 5)
>>> list(nums)
[0, 1, 2, 3, 4]  
# отдаст нам список цифр смотри без 5 и так много где так начинается все с нуля 0 1 2 3 4 

3 Передаем параметры последовательность параметр начало и параметр конца
nums2 = range(2, 6)  # передаем параметры начало и конца нашего списка
>>> nums2
# range(2, 6) вывод
>>> list(nums2)
[2, 3, 4, 5]   # срежет 6  помни последнию цифру всегда срежет возможно 6-2=4 тут как раз 4 элемента

4 Треий параметр это приращение шаги
even = range(0, 11, 2) # промежуток от 0 до 11, приращение на 2 
>>> even
range(0, 11, 2) 
>>> list(even)
[0, 2, 4, 6, 8, 10]  # распечатываю список с каждым шагом 2 до 11 не доходи опять


5 До не включая называется полуоткрытым терминалом
свойства:
1 длина серии разница между концом и началом range(2, 6)  6-2=4  длина серии
2 сращивание двух последовательностей обходится без перекрытия
Пример:

>>> a = range(0, 5)
>>> b = range(5, 10)
>>> both = list(a) + list(b) # объединили два списка
>>> len(both)
10                           # длина списка
>>> both
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   ## 10 не включает помни проэто но промежуток длина состоит из 10(помни про 0)
>>> 

=========================================

Кортежи (tuples)
Кортеж раз создал уже изменить его не получится. Упорядоченное хранение данных.

1 >>> row = ("Geirge", "Guitar")
>>> row
('Geirge', 'Guitar')

2 >>> row2 = ('Paul', 'Bass')
>>> row2
('Paul', 'Bass')

3 Пустые кортеэи очень редки
3.1 empty = tuple()     # первый способ создания пустого кортежа
empty
() 

3.2 
>>> empty = ()       # второй способ создания пустого кортежа
>>> empty
()

4 Кортеж с одним элементом можно создать тремя способами

Первывй способ создания кортежа
>>> one = tuple([1])   # tuple([]) круглые и квадратные скобки 
>>> one
(1,)

Второй способ создания кортежа
 
>>> one = (1, )    # кортеж круглые скобки помни
>>> one
(1,)


Третий способ создания кортежа
>>> one = 1,       # запятая после значения создает кортеж
>>> one
(1,)


5 Круглые скобкки
5.1 Если в круглых скобках заключен один элемент то это как обычные скобки:

>>> d = 3
>>> type(d)
<class 'int'>   # целое значение 

5.2 Если в скобках несколько элементов или есть запятая, то тогда это кортеж
>>> e = (3,)  
>>> type(e)
<class 'tuple'>      # тип кортеж

6. Три способа создания кортежей

Первый способ создания кортежей
>>> p = tuple(['Steph', 'Curry', 'Guard'])  # tuple([]) и тут перечисление значений
>>> p
('Steph', 'Curry', 'Guard')

Второй способ
>>> p = 'Steph', 'Curry', 'Guard'    # просто без скобок перечисление значений
>>> p
('Steph', 'Curry', 'Guard')

Третий способ самый правильный 
>>> p = ('Steph', 'Curry', 'Guard')   # третий способ самый правильный в круглых скобках просто идет перечисление значений 
>>> p
('Steph', 'Curry', 'Guard')

Так как кортежи не изменямы то:
p.append('Golden State') 
AttributeError: 'tuple' object has no attribute
'append'   # у tuple (кортеж) нету такого атрибута как append

Кортежи нужны когда к примеру есть информация которая уже не будет изменяться к примеру фамилия, имя, адрес
Также кортежи меньше используют память, меньше ресурсов в отличии от списков, кортеж может создаться на базе списка, который менять не надо.


На практике они обычно используются для представления записей данных — например, строк, прочитанных из базы данных. В кортежах, представляющих записи данных, могут храниться разные типы
объектов.
=======================================================

Множества (set)  # сами значения можно помещать в {}
Не может иметь дубликатов для этого и используется, множества. Неупорядоченная совокупность объектов где нет дубликатов. используется
для удаления дубликатов и для проверки принадлежности. Можно создать на базе списка.

1 digits = [0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
digit_set = set(digits)
print(digit_set)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}    # удалит лишнию 1 

2 Множества можно создавать в скобках {}
digits = {0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9}
Пример
digits = {0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9}
digits = set(digits)
print(digits)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

digit # обращение в терминале

3 проверка принадлежности объекта в множестве

digits = [0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(9 in digits)
True  # есть 9 в данному множестве

4 odd = {1, 3, 5, 7, 9}

Множества Python поддерживают классические операции теории множеств, такие как объединение ( | ), пересечение ( & ), вычитание ( - ) и
исключающее ИЛИ ( ^ ).

1 Оператор вычитания (-) удаляет элементы входящие в одно множествао из другого множества (по сути сравнивает с первым 
списком(digit_set)  и оставляет только те элементы которых нету в odd)
Пример

digit_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
odd = {1, 3, 5, 7, 9}

even = digit_set - odd
print(even)
{0, 2, 4, 6, 8}   ### выведутся только все из списка digit_set то что не повторяется со списком odd


2 Операция пересечения ( & ) возвращает элементы, присутствующие в обоих множествах: 

even = {0, 8, 2, 4, 6}
prime = set([2, 3, 5, 7])
prime_even = even & prime    ## вернет нам 2 так как 2 есть там и там
print(prime_even)
# 2 


3 Операция объединения ( | ) возвращает множество, состоящее из всех
элементов обоих множеств (с исключением дубликатов):

even = {0, 8, 2, 4, 6}
prime = {10, 32, 3, 6, 4}
numbers = even | prime   # вернет в хаотичном порядке но значение двух множеств без дубликатов
print(numbers)
{0, 32, 2, 3, 4, 6, 8, 10}   # вернет в хаотичном порядке но значение двух множеств без дубликатов



4 Операция исключающего ИЛИ ( ^ ) возвращает множество с элементами,
присутствующими только в одном из двух множеств:

first = set([0, 1, 2, 3, 4])
second = set([2, 3, 4, 5, 6])
in_one = first ^ second
print(in_one)
{0, 1, 5, 6}  # вернет только то что есть только в одном из двух множества

Множества удобно использовать в при объединении и вычитании списков. Также оператор in работает на много быстрее чем для списков. 
Единственный недостаток у множества нету порядка.

Множества являются изменяемыми, но они не упорядочены. Они используются для удаления дубликатов и проверки принадлежности.

==========================================================================

Итерациии 

for конструкция цикла for содержит двоеточие ( : ), за которым следует код с отступом (блок цикла for ). for

1 for letter in ["c", "a", "t"]:   # в цикле for создаться новая переменная letter со своим значением
    print(letter)
c
a  
t
print(letter) ## все символы что были выше уничтожаются остается t
t  # при поторном запуске

В цикле for Python создает новую переменную letter для хранения текущего элемента. Обратите внимание: в letter хранится не индекс,
а строка. Python не очищает переменную после завершения цикла.

2 
animals = ['cat', 'dog', 'bird']
for index in range(len(animals)):    # если len убрать то не сработает так код писать не стоит
    print(index, animals[index])

3 Правильно используем enumerate
''' есть функция enumerate которая умеет range(len)  '''
animals = ['cat', 'dog', 'bird']
for index, value in enumerate(animals):
""" распаковка кортежа происходит засчет созадания двух переменных index(0) и value(cat) таким способом идет распаковка """
    print(index, value)

0 cat
1 dog
2 bird


Выход из цикла когда нам надо
"""Суммиирует числа до тех пор пока не обнаружит отрицательное число"""
numbers = [3, 5, 9, -1, 3, 1]
result = 0
for item in numbers:
    if item < 0:   # ключевой блок пока item меньше нуля
        break
    result += item   ## аналог result = result + item
print(result)
# 17 вывод
Разбор получается, что выводятся следующие значения:
3
5
9
-1       # item дойдет до сих увидит что <0 и цикл прерветься break
3
А так будет происходить следующие 
result += item (result = result + item)
3 + 0= 3
5 + 3 = 8
8 + 9= 17
if item < 0:  ## видит что -1 и все на этом превыается поэтому 17

Если if внутри блока for, то у if 4 пробела,а уже у блока что после if 8 отступов. Блоки могут быть вложенными, и каждый уровень должен иметь свой отступ.
===========================================
Пропуск элементов в цикле


numbers = [3, 5, 9, -1, 3, 1]
result = 0
for item in numbers:
    if item < 0:
        continue
    result += item   ## аналог result = result + item
print(result)
# 21  (3 + 5 + 9 + 3 + 1)

Тоже самое что выше только, если мы дойдем до -1 мы прервем именно эту итерацию и продолжим далее

===========================
Оператор in может использоваться для проверки принадлежности

1 проверяем есть ли в списке значения 
animals = ["cat", "dog", "bird"]
"bird" in animals      # смотрим есть ли в списке данное значение
True

2 Узнать какой индекс 
animals = ["cat", "dog", "bird"]
animals.index('bird')
2  # вывод
============================

Удаление элементов из списков
1 
names = ['John', 'Paul', 'George', 'Ringo']
for name in names:
    if name not in ['John', 'Paul']:
        names.remove(name)

print(names)
['John', 'Paul', 'Ringo']  # цикл дойдет до George и остановиться на этом поэтому Ringo не убрал  

2  Удаление полностью всех значений кроме тех что тебе надо
names = ['John', 'Paul', 'Geroge', 'Ringo']
names_to_remove = []
for name in names:
    if name not in ['John', 'Paul']:
        names_to_remove.append(name)
for name in names_to_remove:
    names.remove(name)

print(names)
['John', 'Paul']  # оставит нам только нужные значения 

3 Удаление при помощи среза
 names = ['John', 'Paul', 'Geroge', 'Ringo']
names_to_remove = []
for name in names[:]:    # copy of names
    if name not in ['John', 'Paul']:
       names.remove(name)

print(names)

==================================

Блок else 

''' проверка являются ли числа положительными '''
positive = False
for num in items:
  if num < 0:
    break                 # блок else выполниться только при условии если цикл  не выполниться на стадии break
else:
  positive = True 

Continue не влияет на выполение блока else 

=====================================
Циклы while 
Блок кода будет выполняться пока некоторое условие остается истинным это while.
за двоеточием : следует блок кода с оступом(Tab) этот блок кода будет выполняться пока результат выражения остается равным True. 
While может создать бесконечный цикл.

1 Пример обратный отсчет 
n = 3 
while n > 0: # пока n > 0 больше нуля
    print(n) # распечатай
    n = n -1  # потом n = n -1 # n станет на 1 меньше и опять пойдет цикл и так до 1 далее уже числа идут n < 0
3
2
1

2 Сознательный выход из цикла , помни while может создавать бесконечный цикл

n = 3
while True:
  print(n)
  n = n - 1 
  if n == 0:                # если n == 0 тогда выходим из цикла также обрати если мы внутри while делаем еще if то у break еще отступ             
      break
3
2
1

=============================

Словари   140 страница