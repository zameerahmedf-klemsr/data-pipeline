import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "scraper.db")

engine = create_engine(f"sqlite:///{db_path}", echo=False)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()