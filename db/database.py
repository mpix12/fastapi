from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import configparser
from Log.logs import log


conf = configparser.ConfigParser()
conf.read_file(open(r'conf/config.conf'))
db_name = conf.get('DATABASE', 'db_name')

SQLALCHEMY_DATABASE_URL = "sqlite:///./"+db_name

log.info(f' DB_URL: {SQLALCHEMY_DATABASE_URL}')

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as exp:
        log.ERROR(f'Unable to connect to DB: {exp}')
    finally:
        db.close()


