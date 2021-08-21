import boto3
from flask_restful import Resource, reqparse

dynamodb_connector = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
user_table_instance = dynamodb_connector.Table('users')


# User class to sign in and sign up the user. It is for user registeration mainly
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

    def post(self):
        data = User.parser.parse_args()
        username = data.get('username')
        password = data.get('password')

        user = user_table_instance.put_item(
                Item={
                    "username": username,
                    "password": password,

                    "Mobile_No_1": 0,
                    "Mobile_No_2": 0,
                    "Landline": 0,
                    "Company_email_address": "NULL",
                    "Personal_email_address": "NULL",
                    "Work_address": "NULL",
                    "Emergency_contact_1": 0,
                    "Emergency_contact_2": 0,
                    "Current_address": "NULL",
                    "Permanent_address": "NULL"
                }
            )

        if user:
            return {"status": "User created successfully"}, 200
        else:
            return {"status": "Unable to create the user"}, 400



    def get(self):
        data = User.parser.parse_args()
        username = data.get('username')
        password = data.get('password')

        user = user_table_instance.get_item(
            Key={
                'username': username,
            }
        )

        if user and str(user.get('Item')['password']) == password:
            return {"username": user.get('Item')['username'], "password": user.get('Item')['password']}, 200
        elif user and user.get('Item')['password'] != password:
            return {"status": "Wrong Credentials"}, 404
        else:
            return {"status": "Unable to get the user"}, 500
