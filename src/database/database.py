from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+mysqlconnector://anhnv:anhnv!@#456@1.53.252.177:3306/healthnet", pool_recycle=3600)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
Base = declarative_base()