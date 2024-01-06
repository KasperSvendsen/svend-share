from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Load the DATABASE_URL environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Check if DATABASE_URL is None
if DATABASE_URL is None:
    raise Exception("DATABASE_URL environment variable is not set")

# Create a database engine with the 'postgresql' dialect
engine = create_engine(DATABASE_URL, client_encoding='utf8', echo=True, connect_args={"sslmode": "disable"})

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
