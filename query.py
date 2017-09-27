from sqlalchemy import func

# count User Records without using a subquery



#this is an update 
UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 8).one()
UrbanVeggieBurger.price = newPrice

TedAddress = session.query(Address).filter_by(employee_id = ted.id).one()
TedAddress.street = "427 Stockton Street"
TedAddress.zip = 94108
session.add(TedAddress)
session.commit()

# delete an item is a 3 step process
# find the entry
# session.delete(entry)
# commit the session
