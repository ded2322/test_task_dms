# Задание 3
Сервер стартует на заданном пользователем порту. Например: notesRest.py —port 5577
Сервис хранит информацию o заметках и предоставляет доступ к ней через REST.

## Используемые технологии
- FastAPI
- SQLAlchemy
- Alembic
-  Docker Compose

## Функциональность
Сервис управления заметками с REST API endpoints:

### Эндпоинты
- `GET /notes/`: Получение всех заметок
- `GET /notes/{id}`: Получение заметки по ID
- `POST /notes/`: Создание новой заметки
- `PUT /tasks/{id}`: Обновление заметки
- `DELETE /tasks/{id}`: Удаление заметки

### Ограничения данных
- `notes`: Строка до 120 символов
- `description`: Строка до 1024 символов

## Развертывание Rest Server

1. ``cd rest_server``
2. ``docker compose up -d``

## Примечания
На ubuntu при использовании ``docker-compose`` может выдать ошибку о конфигах.
Чтобы убрать ошибку нужно использовать ``docker compose``

Так же в прямо в router прописана логика. Сделано с целью упрощения понимания. 

# Тестирование
## Настройка окружения
```bash
# Создание виртуального окружения
python3 -m venv venv

# Активация окружения
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows

# Установка зависимостей
pip install -r requirements.txt
```
## Тестовый запуск performance-теста
### Важно: Перед тестированием убедитесь, что сервис запущен в Docker
```bash
python performance_test.py --url http://localhost:8000 --total 100 --ratio 0.7
```

## Параметры запуска

- --url: базовый URL сервера (по умолчанию http://localhost:8000)

- --total: общее число операций (по умолчанию 100)

- --ratio: доля операций добавления (по умолчанию 0.7)

