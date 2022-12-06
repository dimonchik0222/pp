from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from config import DATABASE_URI
from waitress import serve
from flask_migrate import Migrate
import pymysql
from user import user
from car import car
from rentalcar import RentalCar
from check_models import *
import pytest




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:45155996@localhost:3306/schema'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
engine = create_engine(DATABASE_URI)
mar = Marshmallow(engine)
Session = sessionmaker(bind=engine)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

app.app_context().push()


'''@app.route('/')
def hello_world():
    return 'Hello World! - 28'''

app_test = app.test_client()
if __name__ == '__main__':
    app.run(debug=True)



