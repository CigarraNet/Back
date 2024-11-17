from sqlalchemy import create_engine, MetaData
from decouple import config 

engine = create_engine(config("DATABASE_URL"))

metadata = MetaData()

conn = engine.connect()