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

108