from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


class BaseClass(DeclarativeBase):
	pass


class Task(BaseClass):
	__tablename__ = "task"

	task_id: Mapped[int] = mapped_column(primary_key= True)
	description: Mapped[str] = mapped_column(String(30))

	def __repr__(self) -> str:
		return f"Task(task_id={self.task_id}), description={self.description}"




