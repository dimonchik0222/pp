from models import User, RentalCar, Car
from user import Session

def test():
    session = Session()

    #user = User(id=1, username="savage",fisrtName="Orest", lastName="Chupryna", ,password="1234567890", role=1);

    #session.add(user)

    session.commit()

    session.close()