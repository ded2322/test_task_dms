import re
from collections import Counter
from typing import List, Tuple

def parse_error_codes(log_file_path: str) -> List[Tuple[str, int]]:
    """
    Парсит коды ошибок из лог-файла и подсчитывает их вхождения.

    Функция выполняет следующие основные задачи:
    1. Читает содержимое лог-файла
    2. Извлекает уникальные коды ошибок (5-значные буквенно-цифровые коды)
    3. Подсчитывает количество вхождений каждого кода
    4. Сортирует результаты по убыванию количества вхождений

    Args:
        log_file_path (str): Путь к лог-файлу для анализа.

    Returns:
        List[Tuple[str, int]]: Список кортежей (код_ошибки, количество_вхождений), 
        отсортированный по убыванию.

    Raises:
        FileNotFoundError: Если указанный файл не существует.
        IOError: При ошибках чтения файла.

    Example:
        >>> parse_error_codes('error_log.txt')
        [('test1', 3), ('has3l', 2), ('asfga', 1)]
    """
    # Регулярное выражение для поиска 5-значных буквенно-цифровых кодов
    # \b - граница слова, [a-zA-Z0-9]{5} - точно 5 символов
    error_code_pattern = re.compile(r'\b([a-zA-Z0-9]{5})\b')
    
    # Список для хранения найденных кодов ошибок
    error_codes = []
    
    # Безопасное чтение файла с обработкой возможных ошибок
    try:
        with open(log_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Находим все 5-значные коды в строке
                codes = error_code_pattern.findall(line)
                error_codes.extend(codes)
    
    except FileNotFoundError:
        # Обработка ситуации, когда файл не найден
        print(f"Ошибка: Файл {log_file_path} не найден.")
        return []
    except IOError:
        # Обработка ошибок ввода-вывода
        print(f"Ошибка при чтении файла {log_file_path}.")
        return []
    
    # Подсчет уникальных вхождений с использованием Counter
    error_counts = Counter(error_codes)
    
    # Сортировка по количеству вхождений (от большего к меньшему)
    sorted_error_counts = sorted(
        error_counts.items(), 
        key=lambda x: x[1],  # Сортировка по количеству вхождений
        reverse=True         # От большего к меньшему
    )
    
    return sorted_error_counts

def display_error_codes(error_counts: List[Tuple[str, int]]) -> None:
    """
    Выводит коды ошибок и их количество в консоль.

    Args:
        error_counts (List[Tuple[str, int]]): Список кортежей 
        (код_ошибки, количество_вхождений).

    Example:
        >>> error_counts = [('test1', 3), ('has3l', 2)]
        >>> display_error_codes(error_counts)
        Коды ошибок и их количество:
        test1 : 3
        has3l : 2
    """
    if not error_counts:
        print("Коды ошибок не найдены.")
        return
    
    print("Коды ошибок и их количество:")
    for code, count in error_counts:
        print(f"{code} : {count}")

def main():
    """
    Основная точка входа программы.
    Демонстрирует использование функций парсинга и вывода кодов ошибок.
    """
    # Путь к лог-файлу (может быть передан как аргумент командной строки)
    log_file_path = 'error_log.txt'
    
    # Парсинг кодов ошибок
    error_counts = parse_error_codes(log_file_path)
    
    # Вывод результатов
    display_error_codes(error_counts)

# Точка входа при запуске скрипта напрямую
if __name__ == "__main__":
    main()