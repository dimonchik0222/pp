from flask import Blueprint, request, jsonify, Response
from flask_bcrypt import Bcrypt
from marshmallow import ValidationError
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URI
from schemas import RentalCarSchema
from sqlalchemy import create_engine
from models import RentalCar, User, Car
from user import token_required_user

RentalCar = Blueprint('RentalCar', __name__)
bcrypt = Bcrypt()
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

session = Session()


'''@RentalCar.route('/RentalCar/', methods=['POST'])
@token_required_user
def createRentalCar(current_user):
    if current_user.role ==1:
        return jsonify({'message': 'This is only for users'})
    data = request.get_json(force=True)
    try:
        RentalCarSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    userid = session.query(User).filter_by(id=data['user_id']).first()
    if not userid:
        return Response(status=404, response="user_id doesn't exist")
    carid = session.query(Car).filter_by(id=data['car_id']).first()
    if not carid:
        return Response(status=404, response="car_id doesn't exist")
    session.query(RentalCar).filter_by(beginningDate=data['beginningDate']).first()
    session.query(RentalCar).filter_by(amountOfDays=data['amountOfDays']).first()
    session.query(RentalCar).filter_by(complete=data['complete']).first()
    users = RentalCar(user_id=data['user_id'], car_id=data['car_id'], beginningDate=data['beginningDate'], amountOfDays=data['amountOfDays'], complete=data['complete'])
    session.add(users)
    session.commit()
    session.close()
    return Response(response="RentalCar successfully created")


@RentalCar.route('/RentalCar/<id>', methods=['GET'])
@token_required_user
def getRentalCarById(current_user, id):
    if current_user.role !=1:
        return jsonify({'message': 'This is only for admins'})
    id = session.query(RentalCar).filter_by(id=id).first()
    if not id:
        return Response(status=404, response="Id doesn't exist")
    biblethump = {'id': id.id, 'user_id': id.user_id, 'car_id': id.car_id, 'beginningDate': id.beginningDate, 'amountOfDays': id.amountOfDays}
    return jsonify({'user': biblethump})


@RentalCar.route('/RentalCar', methods=['GET'])
@token_required_user
def getRentalCars(current_user):
    if  current_user.role!=1 :
        return jsonify({'message': 'This is only for admins'})
    limbo = session.query(RentalCar)
    quer = [RentalCarSchema().dump(i) for i in limbo]
    if not quer:
        return {"message": "No RentalCars available"}, 404
    res = {}
    for i in range(len(quer)):
        res[i + 1] = quer[i]
    return res


@RentalCar.route('/RentalCars/<id>', methods=['DELETE'])
@token_required_user
def deleteRentalCar(current_user, id):
    if  current_user.role!=1:
        return jsonify({'message': 'This is only for admins'})
    id = session.query(RentalCar).filter_by(id=id).first()
    if not id:
        return Response(status=404, response="Id doesn't exist")
    session.delete(id)
    session.commit()
    session.close()
    return Response(response="RentalCar successfully deleted")'''

