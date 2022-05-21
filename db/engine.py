"""SQLAlchemy engine for connection to databases"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

import psycopg2


Base = declarative_base()


def postgresql(
    username: str, password: str, host: str, port: int, database: str):
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

    engine = create_engine(
        SQLALCHEMY_DATABASE_URI, echo=False
        )

    return engine