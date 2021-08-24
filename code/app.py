from datetime import timedelta
import datetime

from flask_jwt import JWT
from flask_restful import Api
from flask_cors import CORS

from code.security import authenticate, identity
from resources.user import UserRegister
from resources.user import UserLogin
from flask_lambda import FlaskLambda
from resources.user_personal_info import UserPersonalInfoResource
from resources.user_contact_info import UserContactInfo
from resources.user_educational_info import UserEducationalInfoResource

import db

app = FlaskLambda(__name__)

app.config['SECRET_KEY'] = 'secret12secret12'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=400)
app.config['JWT_NOT_BEFORE_DELTA'] = timedelta(seconds=0)

api = Api(app)
CORS(app)
jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)


@jwt.jwt_payload_handler
def make_payload(payload):
    iat = datetime.datetime.utcnow()
    exp = iat + app.config.get('JWT_EXPIRATION_DELTA')
    nbf = iat + app.config.get('JWT_NOT_BEFORE_DELTA')
    return {
        'username': payload.get('username'),
        'iat': iat,
        'exp': exp,
        'nbf': nbf
    }


api.add_resource(UserRegister, '/user_register')
api.add_resource(UserLogin, '/user_login')
api.add_resource(UserPersonalInfoResource, '/user/personal_info/<string:username>')
api.add_resource(UserEducationalInfoResource, '/user/educational_info/<string:username>')
api.add_resource(UserContactInfo, '/user/contact_info/<string:username>')

db.create_table()
app.run(port=5001)
