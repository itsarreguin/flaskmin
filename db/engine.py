"""SQLAlchemy engine for connection to databases"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

import psycopg2


def postgresql(
    username: str, password: str, host: str, port: int, db: str):
    url = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}'
    
    if not database_exists(url):
        create_database(url)

    engine = create_engine(url, pool_size=100, echo=False)
    return engine


Base = declarative_base()
