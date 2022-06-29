from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

# Function that creates a connection to the database
def database_creation(database_url):
    #Start the database.
    engine = create_engine(database_url, connect_args={'connect_timeout': 60})
    #Generate the database session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Return the session
    return session

