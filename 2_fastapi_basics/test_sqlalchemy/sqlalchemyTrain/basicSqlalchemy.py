import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_str = f"sqlite:///{os.path.join(BASE_DIR, 'basic.db')}"

engine = create_engine(connection_str, echo=True, future=True)

with Session(engine) as session:
    session.execute(text("CREATE TABLE samples (x int, y int)"))
    session.execute(
        text("INSERT INTO samples (x, y) VALUES (:x, :y)"),
        [{'x': 2, 'y': 5}, {'x': 3, 'y': 6}]
    )
    session.commit()
