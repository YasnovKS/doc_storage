# Doc-Storage
'''Для удобства просмотра добавлены стили, БД заполнена и находится в репозитории.'''

Doc-Storage - это тестовое задание на позицию Программист Python в компанию Nsign.
Суть задания - реализовать хранение документов (с полями id, наименование, содержание) с возможностью контроля версий документов
- Версионирование документов реализовано с помощью библиотеки django-reversion
- Хранилище реализовано на бд sqlite3
- Реализована минимальная система авторизации пользователей и минимальные пермишены для возможности создания и редактирования документов
- Созданы шаблоны страниц, применены стили css и скрипт js
- Написаны минимальные тесты для проверки работоспособности CRUD.

## Для возможности проверки работоспособности приложения можно использовать следующие реквизиты для входа: логин test_user, пароль 12345.
## Документы, созданные тестовым юзером помечены в названии.

При необходимости могу в короткие сроки реализовать CI/CD с деплоем в докер-контейнере на удаленном сервере с ос Linux.

## Технологии:

- Python
- Django
- CSS
- JavaScript

## Как это работает?

Склонируйте себе репозиторий проекта, создайте и активируйте виртуальное окружение и установите зависимости с помощью команды "pip install -r requirements.txt".
Создайте и примените миграции с помощью команд:

```Python
python manage.py makemigrations docs
python manage.py migrate
python manage.py createinitialrevisions
```
Создайте суперюзера с помощью команды:
```Python
python manage.py createsuperuser
```
Запустите проект командой:
```Python
python manage.py runserver
```
## Лицензия

#### The MIT License (MIT)

Copyright © «2022» «copyright Yasnov Kirill»

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE

## Авторы
#### Яснов Кирилл
https://github.com/YasnovKS
