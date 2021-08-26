from flask_jwt import jwt_required, current_identity
from flask_restful import Resource
from flask import request
from code.model.user import UserModel


# User class to sign in and sign up the user. It is for user registration mainly
class UserRegister(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()

        if data is None:
            return {'message': 'insufficient arguments'}, 400

        username = data.get('username')
        password = data.get('password')

        if UserModel.get_user(username).get('Item'):
            return {"message": "user already exists"}

        user = UserModel.post_user(username, password)

        if user:
            return {"status": "User created successfully"}, 200
        else:
            return {"status": "Unable to create the user"}, 400


class UserLogin(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        data = request.get_json()

        if data is None or current_identity is None:
            return {'message': 'insufficient arguments'}, 400

        username = data.get('username')
        password = data.get('password')
        user = UserModel.get_user(username).get('Item')
        if user and str(user.get('password')) == password:
            return {"status": '{} successfully logged in.'.format(user.get('username'))}, 200
        else:
            return {"status": "Unable to get the user. Wrong credentials"}, 500