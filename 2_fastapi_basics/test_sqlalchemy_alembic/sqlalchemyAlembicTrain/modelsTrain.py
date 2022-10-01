import os
from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, ForeignKey, text
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    created = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    articles = relationship("Article", back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, firstname={self.firstname!r}, lastname={self.lastname!r})"


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="articles")

    def __repr__(self) -> str:
        return f"Article(id={self.id!r}, name={self.title!r}, fullname={self.content!r})"
