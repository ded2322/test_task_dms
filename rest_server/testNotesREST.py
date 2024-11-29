import requests
import random
import time
import argparse
from concurrent.futures import ThreadPoolExecutor


class PerformanceTester:
    def __init__(self, url, total_ops, add_ratio):
        self.url = url
        self.total_ops = total_ops
        self.add_ratio = add_ratio
        self.notes = []

    def create_note(self):
        data = {
            "notes": f"Test note {random.randint(1, 1000)}",
            "description": f"Description {random.randint(1, 1000)}"
        }
        try:
            response = requests.post(f"{self.url}/notes", json=data)
            return response.json()['id'] if response.status_code == 201 else None
        except Exception:
            return None

    def delete_note(self, note_id):
        try:
            response = requests.delete(f"{self.url}/tasks/{note_id}")
            return response.status_code == 200
        except Exception:
            return False

    def run_test(self):
        start_time = time.time()

        add_count = int(self.total_ops * self.add_ratio)
        delete_count = self.total_ops - add_count

        with ThreadPoolExecutor(max_workers=10) as executor:
            # Создание заметок
            add_results = list(executor.map(lambda _: self.create_note(), range(add_count)))
            self.notes = [note_id for note_id in add_results if note_id]

            # Удаление заметок
            delete_results = list(
                executor.map(self.delete_note, random.sample(self.notes, min(delete_count, len(self.notes)))))

        end_time = time.time()

        print(f"Время теста: {end_time - start_time:.2f} сек")
        print(f"Создано заметок: {len([n for n in add_results if n])}")
        print(f"Удалено заметок: {sum(delete_results)}")


def main():
    parser = argparse.ArgumentParser(description="Тест производительности REST API")
    parser.add_argument("--url", default="http://localhost:8000", help="URL сервера")
    parser.add_argument("--total", type=int, default=100, help="Количество операций")
    parser.add_argument("--ratio", type=float, default=0.7, help="Доля добавления")

    args = parser.parse_args()
    tester = PerformanceTester(args.url, args.total, args.ratio)
    tester.run_test()


if __name__ == "__main__":
    main()