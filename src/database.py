import os
from typing import Annotated
from dotenv import load_dotenv
from fastapi.params import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker


""" Set Enviroment Variables """
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", default="sqlite:///./bucketier.db")


""" Main """
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_database():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()

DatabaseSession = Annotated[Session, Depends(get_database)]
