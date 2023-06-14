from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

POSTGRESQL_DATABASE_URL = 'postgresql://postgres:postgres@localhost/TodoApplicationDatabase'

MYSQL_DATABASE_URL = 'mysql+pymysql://root:mysql@127.0.0.1:3306/todoapplicationdatabase'

engine = create_engine(POSTGRESQL_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


