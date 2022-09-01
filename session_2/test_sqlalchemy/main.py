from sqlalchemy import Column, Integer, String, DateTime, create_engine
from datetime import datetime
from sqlalchemy.orm import declarative_base
import os

Base = declarative_base() 


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string=f"sqlite:///{os.path.join(BASE_DIR, 'site.db')}"
engine=create_engine(connection_string, echo=True)

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name  = Column(String, nullable=False)
    birth = Column(DateTime)
    created = Column(DateTime, default= datetime.utcnow)

    def __repr__(self):
        return (
                f'UserModel(id={self.id}, first_name={self.first_name})'
                )


