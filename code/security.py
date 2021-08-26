from code.key_generator import Keys
from code.model.user import UserModel


def authenticate(username, password):
    user = UserModel.get_user(username).get('Item')
    if user and (Keys.decrypt_message(user.get("password").encode("utf-8")).decode("utf-8")) == password:
        return user


def identity(payload):
    username = payload.get('username')
    return UserModel.get_user(username)
