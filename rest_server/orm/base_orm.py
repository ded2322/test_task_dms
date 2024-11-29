from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import SQLAlchemyError

from utils.database import async_session_maker
from models.models import Notes

class BaseOrm:
    model = Notes

    @classmethod
    async def show_all_notes(cls):
        """
        Выборка всех данных из таблицы, отдает в виде списка словарей
        """
        async with async_session_maker() as session:
            """
            SELECT * FROM csl.model;
            """
            query = select(cls.model.id, cls.model.note)
            result = await session.execute(query)
            return result.mappings().all()


    @classmethod
    async def found_one_or_none(cls, **kwargs):
        """
        Находит строку в таблице, отдает в виде словаря
        """
        async with async_session_maker() as session:
            """
            SELECT * FROM csl.model
            WHERE **kwargs;
            """

            query = select(cls.model.__table__.columns).filter_by(**kwargs)
            result = await session.execute(query)
            return result.mappings().one_or_none()


    @classmethod
    async def insert_data(cls, **kwargs):
        """
        Добавляет данные в таблицу
        """
        async with async_session_maker() as session:
            """
            INSERT INTO csl.model VALUES
            (**kwargs);
            """

            query = insert(cls.model).values(**kwargs).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return result.scalar_one()

    @classmethod
    async def update_data(cls, id: int, **kwargs):
        """
        Обновляет данные в таблице.
        Принимает id строки которую нужно обновить,
        столбец который нужно обновить
        новые данные которые нужно вставить в этот столбец
        """
        async with async_session_maker() as session:
            """
            UPDATE csl.model
            SET column = new_data;
            """
            query = update(cls.model).where(cls.model.id == id).values(**kwargs)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete_data(cls, **kwargs):
        """
        Удаляет данные из таблицы
        """
        async with async_session_maker() as session:
            """
            DELETE FROM csl.model
            WHERE **kwargs
            """

            query = delete(cls.model).filter_by(**kwargs)
            await session.execute(query)
            await session.commit()
