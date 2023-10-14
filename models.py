import os

from sqlalchemy import JSON, Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

PG_DSN = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_async_engine(PG_DSN)
Session = sessionmaker(class_=AsyncSession, expire_on_commit=False, bind=engine)

Base = declarative_base()


class SwapiPeople(Base):
    __tablename__ = "swapi_people"

    id = Column(Integer, primary_key=True)
    person_id = Column(JSON)
    films = Column(String)
    eye_color = Column(String)
    birth_year = Column(String)
    species = Column(String)
    skin_color = Column(String)
    name = Column(String)
    mass = Column(String)
    homeworld = Column(String)
    height = Column(String)
    hair_color = Column(String)
    gender = Column(String)
    starships = Column(String)
    vehicles = Column(String)


Base = declarative_base()
