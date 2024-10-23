# backend/app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import time
from sqlalchemy.exc import OperationalError

load_dotenv()

POSTGRES_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/app_db")
MAX_RETRIES = 5
RETRY_DELAY = 5  # seconds

# Function to create engine with retry logic
def create_db_engine():
    for attempt in range(MAX_RETRIES):
        try:
            engine = create_engine(POSTGRES_URL)
            # Verify connection
            engine.connect()
            print("Database connection successful!")
            return engine
        except OperationalError as e:
            if attempt < MAX_RETRIES - 1:
                print(f"Database connection attempt {attempt + 1} failed. Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                print("Max retries reached. Could not connect to database.")
                raise e

engine = create_db_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()