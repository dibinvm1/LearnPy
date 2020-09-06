import sys

from sqlalchemy import Column, ForeignKey,Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'
    r_id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False)
class MenuItem(Base):
    __tablename__ = 'menu_item'

    
    m_id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer,ForeignKey('restaurant.r_id'))
    restaurant = relationship(Restaurant)

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)





