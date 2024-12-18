from sqlalchemy import Column, String, Integer, String, Boolean
from sqlalchemy.dialects.mysql import CHAR
from app.app_db import Base

class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False, nullable=False)

    def __init__(self, title: str, completed: bool):
        self.title = title
        self.completed = completed

    def __repr__(self):
        return (f"<OIDCRequest(id={self.id}, title={self.title}, completed={self.completed})>")

    def as_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'completed': self.completed
        }