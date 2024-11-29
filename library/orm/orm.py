from sqlalchemy import insert
from sqlalchemy.exc import SQLAlchemyError

from utils.database import async_session_maker

class BaseOrm:
    model = None

    async def insert_data(cls, **kwargs):
            """
            Добавляет данные в таблицу
            """
            async with async_session_maker() as session:
                '''"""
                INSERT INTO csl.model VALUES
                (**kwargs);
                """'''
                try:
                    query = insert(cls.model).values(**kwargs)
                    result = await session.execute(query)
                    inserted_id = result.inserted_primary_key[0]
                    await session.commit()
                    return inserted_id
                except (SQLAlchemyError, Exception) as e:
                    if isinstance(e, SQLAlchemyError):
                        print(f"SQLAlchemy exc in insert_data: {str(e)}")
                    else:
                        print(f"Unknown exc in insert_data: {str(e)}")