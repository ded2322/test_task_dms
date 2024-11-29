from orm.orm import BaseOrm
from models.models import Books, Author, Reader, ReadingRoom, InfoBook, BusyBook
import asyncio

class DataSeeder:
    def __init__(self):
        self.author_orm = BaseOrm()
        self.author_orm.model = Author
        
        self.books_orm = BaseOrm()
        self.books_orm.model = Books
        
        self.reader_orm = BaseOrm()
        self.reader_orm.model = Reader
        
        self.reading_room_orm = BaseOrm()
        self.reading_room_orm.model = ReadingRoom
        
        self.info_book_orm = BaseOrm()
        self.info_book_orm.model = InfoBook
        
        self.busy_book_orm = BaseOrm()
        self.busy_book_orm.model = BusyBook

    async def seed_authors(self):
        authors = ['Харуки Мураками','Агата Кристи','Стивен Кинг']       
        for author_name in authors:
            await self.author_orm.insert_data(name=author_name)

    async def seed_reading_rooms(self):
        reading_rooms = [101, 201]
        for room_number in reading_rooms:
            await self.reading_room_orm.insert_data(reading_room=room_number)

    async def seed_books(self):
        books_data = [
            {'title': 'Норвежский лес', 'id_reading_room': 1},
            {'title': 'Десять негритят', 'id_reading_room': 1},
            {'title': 'Ловец снов', 'id_reading_room': 2},
        ]
        for book_info in books_data:
            await self.books_orm.insert_data(**book_info)

    async def seed_book_authors(self):
        book_authors = [
            {'id_book': 1, 'id_author': 1},  # Мураками - Норвежский лес
            {'id_book': 2, 'id_author': 2},  # Кристи - Десять негритят
            {'id_book': 3, 'id_author': 3},  # Кинг - Ловец снов
        ]
        for book_author in book_authors:
            await self.info_book_orm.insert_data(**book_author)

    async def seed_readers(self):
        readers = ['Алиса', 'Боб']
        for reader_name in readers:
            await self.reader_orm.insert_data(name=reader_name)

    async def seed_reader_books(self):
        reader_books = [
            {'id_book': 1, 'id_reader': 1},  # Алиса - Норвежский лес
            {'id_book': 2, 'id_reader': 1},  # Алиса - Десять негритят
            {'id_book': 3, 'id_reader': 2}   # Боб - Ловец снов
        ]
        for reader_book in reader_books:
            await self.busy_book_orm.insert_data(**reader_book)

    async def seed_all_data(self):
        await self.seed_authors()
        await self.seed_reading_rooms()
        await self.seed_books()
        await self.seed_book_authors()
        await self.seed_readers()
        await self.seed_reader_books()
        print("All data added successfully")

async def main():
    seeder = DataSeeder()
    await seeder.seed_all_data()

if __name__ == "__main__":
    asyncio.run(main())