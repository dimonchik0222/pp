from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Boolean
from sqlalchemy.ext.declarative import declarative_base
from config import DATABASE_URI
Base = declarative_base()

engine = create_engine(DATABASE_URI)

class User(Base):
    __tablename__ = "User"
    id = Column(Integer(),primary_key=True, unique=True, autoincrement=True)
    username = Column(String(100))
    firstName = Column(String(100))
    lastName = Column(String(100))
    Phone = Column(String(100))
    password = Column(String(100))
    role = Column(Integer())
    def __repr__(self):
        return "<User(username = '{}',firstName='{}', lastName = '{}', Phone = '{}')>" \
            .format(self.username, self.firstName, self.lastName, self.Phone)

class RentalCar(Base):
    __tablename__ = "RentalCar"
    id = Column(Integer(),primary_key=True, unique=True, autoincrement=True)
    Price_for_1d = Column(Integer())
    Days = Column(Integer())
    user_id = Column(Integer())
    car_id = Column(Integer())
    def __repr__(self):
        return "<RentalCar(Price_for_1d='{}', Days={}, user_id='{}', car_id='{}')>" \
            .format(self.Price_for_1d, self.Days, self.user_id, self.car_id)

class Car(Base):
    __tablename__ = "Car"
    id = Column(Integer(),primary_key=True, unique=True, autoincrement=True)
    Brand = Column(String(100))
    Model = Column(String(100))
    Year = Column(Integer())
    FuelConsumption = Column(String(100))
    Status = Column(String(100))
    def __repr__(self):
        return "<Car(brand='{}', model='{}', Year ='{}', FuelConsumption ='{}',status='{}')>" \
            .format(self.brand, self.model, self.year, self.FuelConsumption,self.status)



