from flask import Flask
from flask_restful import Api
from resources.user import UserRegister
from resources.user import UserLogin
from flask_lambda import FlaskLambda
from flask_cors import CORS
from resources.user_personal_info import UserPersonalInfoResource
from resources.user_contact_info import UserContactInfo
from resources.user_educational_info import UserEducationalInfoResource
from security import authenticate, identity

import db

app = FlaskLambda(__name__)
api = Api(app)


api.add_resource(UserRegister, '/user')
api.add_resource(UserLogin, '/user/<string:username>')
api.add_resource(UserPersonalInfoResource, '/user/personal_info/<string:username>')
api.add_resource(UserEducationalInfoResource, '/user/educational_info/<string:username>')
api.add_resource(UserContactInfo, '/user/contact_info/<string:username>')

db.create_table()
app.run(port=5001)
