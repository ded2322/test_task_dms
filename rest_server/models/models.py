from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import Base

class Notes(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    note: Mapped[String] = mapped_column(String(length=120))
    description: Mapped[String] = mapped_column(String(length=1024))