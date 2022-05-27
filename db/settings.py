from sqlalchemy.orm import scoped_session, sessionmaker

from decouple import config

from db.engine import postgresql, Base


engine = postgresql(
    username=config('POSTGRESQL_USER'),
    password=config('POSTGRESQL_PASSWORD'),
    host=config('POSTGRESQL_HOST'),
    port=config('POSTGRESQL_PORT'),
    database=config('POSTGRESQL_DB')
)


db_session = scoped_session(
    sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
)


Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)


def cls_db():
    Base.metadata.clear()


def drop_db():
    Base.metadata.drop_all(bind=engine)