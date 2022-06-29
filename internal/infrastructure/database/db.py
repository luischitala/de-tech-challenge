import os
# ORM dependencies
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Engine creation
engine = create_engine("postgresql://docker:docker@db:5432/gis")
metadata = MetaData(engine)
# Session configuration
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# Function that will be a dependency for the database interactions from the controllers
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()