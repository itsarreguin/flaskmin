from sqlalchemy.orm import scoped_session, sessionmaker

from db.engine import postgresql, Base


engine = postgresql(
    username='itsarreguin',
    password='adreno',
    host='localhost',
    port=5432,
    database='flaskmin'
)

db_session = scoped_session(
    sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
)


Base.query = db_session.query_property()


def init_db():
    from app import models
    Base.metadata.create_all(bind=engine)


def cls_db():
    from app import models
    Base.metadata.create_all(bind=engine)


def drop_db():
    from app import models
    Base.metadata.drop_all(bind=engine)