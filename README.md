### Проект Yatube API - это учебный проект, который показывает базовые возможности API на DRF

```
API даёт практически полный набор функций для работы с сервисом YATUBE.
```
Сервис Yatube - социальная сеть для обмена постами, написанная на Python 3 с использованием Django. Поддерживает размещение постов с текстом, картинкой, возможности подписок на автора, оставления комментариев.
```
Основные функции:
Создание и удаление постов, получение списка постов, списка комментариев к конкретному посту, редактирование комментариев.

Полный список доступных функций доступен в ReDOc по ссылке ниже

```

### Список использованных технологий при разработке:
```
Python
```
Django
```
djangorestframework
```
djangorestframework-simplejwt
```
Pillow
```
requests
```
```
### Как запустить проект Yatube Api:

```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Примеры запросов к API:

```
/api/v1/posts/   -> ответ:  
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

### Ссылка на REDOC при запуске локального сервера:

http://127.0.0.1:8000/redoc/

### Автор: Федор Абаза