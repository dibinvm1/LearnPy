from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session1 = DBSession()

def getAllRestaurentNames():
    return ([rinfo for rinfo in session1.query(Restaurant.r_id,Restaurant.name)])

def getNameFromId(res_id):
    rest = session1.query(Restaurant).filter_by(r_id = res_id).one()
    return (rest.name)

def addRestaurantToDB(restName):
    restaurant = Restaurant(name = restName)
    session1.add(restaurant)
    session1.commit()

def deleteRestaurantFromDB(res_id):
    rest = session1.query(Restaurant).filter_by(r_id = res_id).one()
    session1.delete(rest)
    session1.commit()

def renameRestaurantInDB(res_id,newName):
    rest = session1.query(Restaurant).filter_by(r_id = res_id).one()
    rest.name = newName
    session1.add(rest)
    session1.commit()

#print(len(getAllRestaurentNames()))
#print(getAllMenuItemNames())