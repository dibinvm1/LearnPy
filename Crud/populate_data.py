from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base ,Restaurant , MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession  = sessionmaker(bind=engine)
session = DBSession()

MyFirstRestaurant = Restaurant(name="Pizza Plaza")
#session.add(MyFirstRestaurant)
#session.commit()

#cheesePizza = MenuItem(name = "Cheese Pizza",description = "Pizza with Lots of Mozzarella cheese",course = "Entree",price = "8.99",restaurant = MyFirstRestaurant)

#session.add(cheesePizza)
#session.commit()

items = session.query(MenuItem).all()

for item in items:
    print(item.name)