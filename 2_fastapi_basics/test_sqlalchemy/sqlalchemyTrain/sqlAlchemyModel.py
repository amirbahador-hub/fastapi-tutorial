import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, relationship, declarative_base
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_str = f"sqlite:///{os.path.join(BASE_DIR, 'model.db')}"

engine = create_engine(connection_str, echo=True, future=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)

    articles = relationship("Article", back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, firstname={self.firstname!r}, lastname={self.lastname!r})"


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="articles")

    def __repr__(self) -> str:
        return f"Article(id={self.id!r}, name={self.title!r}, fullname={self.content!r})"