import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelsTrain import User as UserModel, Article as ArticleModel


class Query:

    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        connection_str = f"sqlite:///{os.path.join(BASE_DIR, 'modelsTrain.db')}"
        self.session_maker = sessionmaker(bind=create_engine(connection_str, echo=True, future=True))


query = Query()

users = [UserModel(firstname="ali", lastname="qasemi"), UserModel(firstname="hasan", lastname="safari")]
articles = [ArticleModel(title="news1", content="content news1", user=users[0]),
            ArticleModel(title="news2", content="content news2", user=users[1])]

with query.session_maker() as session:
    for user in users:
        session.add(user)
    for article in articles:
        session.add(article)
    session.commit()
