# Обрезка ссылок с помощью Битли

Сокращает ссылки с помощью сервиса (bitly.com), и выдаёт количество нажатий по ним.

### Как установить

Для работы программы требуется API ключ (bitly.com), создайте API ключ (bitly.com) и запишите его в в файле .env (BITLY_TOKEN=ваш ключ).
Вот как он выглядит: 6354dbbb6d2473g56ob4b6abfc94542585re840h

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```


### Пример работы программы
C:\Users\Никита\PycharmProjects\clicks> main.py https://www.youtube.com
Битлинк: bit.ly/3z6dErY

C:\Users\Никита\PycharmProjects\clicks>main.py bit.ly/3z6dErY
Количество переходов: 0


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

