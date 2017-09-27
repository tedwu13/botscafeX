from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurants.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)


