from sqlalchemy import Column, Integer, String, DateTime, create_engine
from datetime import datetime
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base() 

# alembic init migrations
# change alembic ini --> sqlalchemy.url = sqlite:///models.db
# change env --> from models import Base \n terget_metadata = Base.metadata
# alembic revision --autogenerate -m "Create user model"

class UerModel(Base):
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

users = [
        UerModel(first_name="Aryan", last_name="Eqbal", birth=datetime(1998, 7, 6)),
        UerModel(first_name="Hossein", last_name="Ayat", birth=datetime(1980, 5, 5))
        ]

session_maker = sessionmaker(bind=create_engine('sqlite:///models.db'))

def create_users():
    with session_maker() as session:
        for user in users:
            session.add(user)
        session.commit()

with session_maker() as session:
    users_records = session.query(UerModel).all()
    for user in users_records:
        print(user)
