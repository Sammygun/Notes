1 python это программа которая интепретирует код

2 https://trinket.io/python3 # где можно выполнять код

3  https://stepik.org/course/67/promo # сам курс

4 http://wombat.org.ua/AByteOfPython/ ## укус питона с удобным поиском

5 https://docs.python.org/3/ ## документация python официальная

6 https://serverspace.by/support/help/ustanovka-jupyter-notebook-na-ubuntu/
установка jupyter ustanovka-jupyter
sudo apt update
sudo apt upgrade
sudo apt install python3-pip python3-dev # устанавливается pip вместе с файлами заголовка Python
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
mkdir ~/Serverspace # по желанию
cd ~/Serverspace
virtualenv Serverspace
pip install jupyter

1.3https://conda.io/en/latest/miniconda.html
bash Miniconda.. ## запуск скаченного файла
 /home/sam/miniconda3

1.4 Устнаовка  jupyter notebook !!!! правильная версия
pip install -- upgrade pip # в папке stepik

4) Далее вводим pip install jupyter

5) Запускаем - вводим jupyter notebook # после ввода команды в терминале в  браузере откроется

============================================================
1 Работа с числами
1 Помни произведения деление в приоритете  при простом работе с числами однако если есть скобки то первые скобки
2 40 // 5 # целочисленное деление будет всегда целое число 8
  40 // 6 # вернет 6 (6*6 = 36)
3 42 % 8 ## вернуть остаток после деления 2 (5*8=40 42 - 40 = 2)

4 239 % 10 ## вывод 9 будет
  239 // 10 ### вывод 23(а не 23б9)

5 2 ** 5 # возведение в пятю степень

6 + 42 #  вывод 42
  -42  #  вывод -42

7 +-+42 ## -42 вывод
8 -* 42 ## будет ошибка SyntaxError
SyntaxError # правила синтаксиса нарушены подсветит строку с проблемой

9 5 // 0 # ZeroDivisionError: integer division or modulo by zero
# на ноль делить не можем