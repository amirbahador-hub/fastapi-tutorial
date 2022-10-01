from sqlAlchemyModel import engine, Base

Base.metadata.create_all(engine)
