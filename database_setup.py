import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

 
Base = declarative_base()
 
class Restaurant(Base):
    __tablename__ = 'restaurant'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
 
class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True) #uniquely identify the sql table
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer,ForeignKey('restaurant.id')) #create a restaurant id
    restaurant = relationship(Restaurant) #establish a relationship between a restaurant and menu




### insert at end of file ###
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
