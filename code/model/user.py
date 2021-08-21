import boto3


# Get the service resource.

class UserModel:
    dynamodb_connector = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    user_table_instance = dynamodb_connector.Table('users')

    @staticmethod
    def post_user(username, password):
        user = UserModel.user_table_instance.put_item(
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

        return user

    @staticmethod
    def get_user(username):
        user = UserModel.user_table_instance.get_item(
            Key={
                'username': username,
            }
        )
        return user
