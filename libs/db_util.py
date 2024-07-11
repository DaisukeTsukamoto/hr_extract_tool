from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Database:
    def setup():
        engine = create_engine('sqlite:///scraped_data.db')
        Base.metadata.create_all(engine)
        return sessionmaker(bind=engine)()

class HrInfo(Base):
    __tablename__ = 'hr_info'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(String)
    body = Column(String)
