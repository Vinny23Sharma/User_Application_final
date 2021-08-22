from flask_restful import Resource, reqparse
from code.model.user import UserModel


# User class to sign in and sign up the user. It is for user registration mainly
class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()
        username = data.get('username')
        password = data.get('password')

        user = UserModel.post_user(username, password)

        if user:
            return {"status": "User created successfully"}, 200
        else:
            return {"status": "Unable to create the user"}, 400

    @classmethod
    def get(cls):
        data = cls.parser.parse_args()
        username = data.get('username')
        password = data.get('password')

        user = UserModel.get_user(username).get('Item')

        if user and str(user['password']) == password:
            return {"username": user['username'], "password": user['password']}, 200
        elif user and user['password'] != password:
            return {"status": "Wrong Credentials"}, 404
        else:
            return {"status": "Unable to get the user"}, 500
