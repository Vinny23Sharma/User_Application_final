from flask_restful import Resource, reqparse

from code.model.user import UserModel


# User class to sign in and sign up the user. It is for user registration mainly
class UserRegister(Resource):
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


class UserLogin(Resource):
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
    def post(cls, username):

        user_authentication_data = cls.parser.parse_args()
        user = UserModel.get_user(username).get('Item')
        if user and str(user['password']) == user_authentication_data.get("password"):
            return {"username": user['username'], "password": user['password']}, 200
        else:
            return {"status": "Unable to get the user. Wrong credentials"}, 500
