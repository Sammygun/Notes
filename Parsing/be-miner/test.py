import requests
import lxml.html
from lxml import etree

def get_titles(html_text):
    tree = lxml.html.document_fromstring(html_text)
    """ lxml.html модуль вызываем ее функцию которая передаст html документ"""
    text_titles = tree.xpath("//*[@class='entry-title']/a/text()")
    text_contents = tree.xpath("//*[@class='entry-content entry-excerpt clearfix']/p/text()")
    """ потому что это параграф класса поэтому  p text  выдернуть конкретный """
    return text_titles, text_contents

html_text = requests.get("https://be-miner.info/") # глобальная переменная та что выше в функции находится
if html_text.status_code == 200: # если статус 200 то 
    text_title, text_content = get_titles(html_text.text) ## то выведи функцию get_titles c text
    #print(text_title, text_content)
    for i, t in enumerate(text_title):
        text = """
        ========================
        Заголовок ---- {title}
        Контент   ---- {content}
        ========================""".format(title=t, content=text_content[i])
        print(text)





"""
1 <a href="https://be-miner.info/bitgreen-nastrojka-masternody-v-novom-blokchejne/" rel="bookmark">Bitgreen настройка мастерноды в новом блокчейне</a>

2 ("//*[@class='entry-title']/a/text()") # смотрю какой класс у нашей ссылки указываю, ссылка /a/text() выдерни нам текст

3 ModuleNotFoundError: No module named 'lxml # решение ошибки 
1 python3 -m venv venv # в папке проекта
2 source venv/bin/activate # активировал 
3 pip install lxml
4 pip install requests


<div class="entry-content entry-excerpt clearfix">
		<p>В общем разработчики BitGreen малость намудрили с настройкой мастерноды, поэтому давайте разбираться. Скачаем новый кошелек ( на текущий момент версия 1.4.0.3 ) из оф. репозитория. Дальше все как обычно — нужно создать адрес (адрес можно …</p>
		
		<a href="https://be-miner.info/bitgreen-nastrojka-masternody-v-novom-blokchejne/" class="more-link">Дальше »</a>

			</div>

"""