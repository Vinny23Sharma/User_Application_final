from code.key_generator import Keys
from code.settings import user_table_instance


# Get the service resource.

class UserModel:
    @classmethod
    def post_user(cls, username, password):

        encrypted_message = Keys.encrypt_message(password).decode("utf-8")

        user = user_table_instance.put_item(
            Item={
                "username": username,
                "password": encrypted_message,
            }
        )

        return user

    @classmethod
    def get_user(cls, username):
        user = user_table_instance.get_item(
            Key={
                'username': username,
            }
        )
        return user

