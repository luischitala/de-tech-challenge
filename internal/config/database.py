"""coding=utf-8."""
 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator, Callable

from sqlalchemy import create_engine, orm

from internal.config import settings
from internal.entity.base import Base
# from package.sqlalchemy import get_session

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:TaekoBB@localhost:5432/postgres"
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()


