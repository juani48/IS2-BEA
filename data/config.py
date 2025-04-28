#basedir = os.path.abspath(os.path.dirname(__file__))
#DEBUG = True
#SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'db', 'database.db')}"
#SQLALCHEMY_TRACK_MODIFICATIONS = False

import os	
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = os.path.abspath(os.path.dirname(__file__))
DB_FILE = "database.db"
engine = create_engine(f"sqlite:///{os.path.join(DB_PATH, 'db', DB_FILE)}")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()