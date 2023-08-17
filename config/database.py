import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_database = '../database.sqlite'
#read the current directory
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f'sqlite:///{os.path.join(base_dir, sqlite_database)}'

engine = create_engine(database_url,echo=True ,connect_args={"check_same_thread": False})

session = sessionmaker(bind=engine)

base = declarative_base()