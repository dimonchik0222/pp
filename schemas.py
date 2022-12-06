from marshmallow import Schema, fields


class UserSchema(Schema):
    username = fields.String()
    firstName = fields.String()
    lastName = fields.String()
    phone = fields.String()
    password = fields.String()
    role = fields.String()


class RentalCarSchema(Schema):
    Price_for_1d = fields.Integer()
    Days = fields.Integer()
    user_id = fields.Integer()
    car_id = fields.Integer()


class CarSchema(Schema):
    Brand = fields.String()
    Model = fields.String()
    Year = fields.Integer()
    FuelConsumption = fields.String()
    status = fields.String()
