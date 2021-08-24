from code.model.user import UserModel


def authenticate(username, password):
    user = UserModel.get_user(username).get('Item')
    if user and str(user['password']) == password:
        return user


def identity(payload):
    _id = payload['identity']
    return UserModel.find_by_userid(_id)
