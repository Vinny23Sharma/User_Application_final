import boto3


# Get the service resource.

class UserModel:
    dynamodb_connector = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    user_table_instance = dynamodb_connector.Table('users')

    @classmethod
    def post_user(cls, username, password):
        user = cls.user_table_instance.put_item(
            Item={
                "username": username,
                "password": password,
            }
        )

        return user

    @classmethod
    def get_user(cls, username):
        user = cls.user_table_instance.get_item(
            Key={
                'username': username,
            }
        )
        return user
