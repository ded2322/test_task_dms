# Задача 1

Создать схему базы данных «Библиотека» с сущностями: Книга, Автор, Зал, Читатель. Один автор
может написать несколько книг, у книги может быть несколько авторов. Конкретная книга может
размещаться в одном зале, в одном зале размещается множество книг. Читатель может брать
одновременно несколько книг.

## Сущности базы данных
- Books: Информация о книгах
- Author: Данные об авторах 
- Reader: Информация о читателях
- ReadingRoom: Информация о залах библиотеки
- InfoBook: Дополнительная информация о книгах
- BusyBook: Отслеживание занятых книг

## Связи между сущностями
- Один автор может написать несколько книг
- Одна книга может иметь несколько авторов
- Конкретная книга размещается в одном зале
- В одном зале может размещаться множество книг
- Читатель может одновременно брать несколько книг

## Используемые технологии
- Язык: Python 3.10
- ORM: SqlAlchemy
- Миграции: Alembic
- Контейнеризация: Docker Compose

## Запуск проекта
1. Перейти в директорию проекта: `cd library`
2. Собрать и запустить контейнеры: `docker compose up --build`

### Примечание
В случае выдачи ошибки о том, что нет команды ``docker compose``

На используйте на Ubuntu команду:

``sudo apt install docker-compose-v2``

## Подключение к базе данных
Параметры подключения:
- База данных: library_db
- Пользователь: admin
- Пароль: admin
- Хост: localhost
- Порт: 5432

Для подключения к контейнеру с базой данных:
1. Команда для входа в контейнер
```bash 
docker exec -it library_db psql -U admin -d library_db
```
2. Команда для просмотра созданных таблиц
```bash 
\dt
```

## Структура проекта
library/
├── models/          # SQLAlchemy модели базы данных
├── migrations/      # Alembic миграции
├── scripts/         # Скрипты для заполнения базы данных
├── docker-compose.yml
└── Dockerfile
```
