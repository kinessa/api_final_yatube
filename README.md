## api_final
api_final_yatube - это API для соц. сети
***
### возможности:
* создавать посты
* подписываться на авторов
* комментировать посты
* авторизация по токену
*** 
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/kinessa/api_final_yatube.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
***
Ссылка на локальный сервер:
http://127.0.0.1:8000/

Документация доступна по адресу:
http://127.0.0.1:8000/redoc/
***
###Пример работы API:

Запрос для создания поста:
```python
import requests
url = 'http://127.0.0.1:8000/api/v1/posts/'
TOKEN = 'Тут ваш токен'

data = {
  "text": "Здесь ваш текст",
}
headers = {'Authorization': f'Bearer {TOKEN}'}
request = requests.post(url, headers=headers, data=data)
```
Ответ от API:
```json
{
    "author": "string",
    "group": "None",
    "id": 1,
    "image": "None",
    "pub_date": "2021-08-17T02:37:42.283465Z",
    "text": "Здесь ваш текст"
}
```
***
