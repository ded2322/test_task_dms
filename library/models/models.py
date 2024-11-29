from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import Base

class Books(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[String] = mapped_column(String(length=120))
    id_reading_room: Mapped[int] = mapped_column(ForeignKey("reading_room.id", ondelete="CASCADE"))

class Author(Base):
    __tablename__ = "author"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String(length=120), nullable=False)
    


class Reader(Base):
    __tablename__ = "reader"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String(length=120), nullable=False)


class ReadingRoom(Base):
    __tablename__ = "reading_room"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    reading_room: Mapped[int]


class InfoBook(Base):
    __tablename__ = "info_book"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_book: Mapped[int] = mapped_column(ForeignKey("book.id", ondelete="CASCADE"))
    id_author: Mapped[int] = mapped_column(ForeignKey("author.id", ondelete="CASCADE"))

    

class BusyBook(Base):
    __tablename__ = "busy_book"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_book: Mapped[int] = mapped_column(ForeignKey("book.id", ondelete="CASCADE"))
    id_reader: Mapped[int] = mapped_column(ForeignKey("reader.id", ondelete="CASCADE"))
    