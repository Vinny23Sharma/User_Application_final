from flask_jwt import current_identity, jwt_required
from flask_restful import Resource
from flask import request
from code.model.user_contact_info import UserContactModel


class UserContactInfo(Resource):

    @classmethod
    @jwt_required()
    def post(cls, username):
        data = request.get_json()

        if data is None or current_identity is None:
            return {'message': 'insufficient arguments'}, 400

        user = UserContactModel.put_user_contact(username, data)

        if user:
            return {"status": "User contact info created successfully"}, 200
        else:
            return {"status": "Unable to create the user contact info"}, 400

    @classmethod
    @jwt_required()
    def get(cls, username):
        try:
            user = UserContactModel.get_user_contact(username)
            data = user.get('Item')

            if data is None or current_identity is None:
                return {'message': 'insufficient arguments'}, 400

            if data.get('Personal_email_address'):
                return {
                           'Mobile_No_1': int(data.get('Mobile_No_1')),
                           'Mobile_No_2': int(data.get('Mobile_No_2')),
                           'Landline': int(data.get('Landline')),
                           'Company_email_address': data.get('Company_email_address'),
                           'Personal_email_address': data.get('Personal_email_address'),
                           'Work_address': data.get('Work_address'),
                           'Emergency_contact_1': int(data.get('Emergency_contact_1')),
                           'Emergency_contact_2': int(data.get('Emergency_contact_2')),
                           'Current_address': data.get('Current_address'),
                           'Permanent_address': data.get('Permanent_address')
                       }, 200
            else:
                return {"status": "Unable to get the user contact info"}, 500
        except:
            return {"status": "Unable to get the user contact info"}, 500

    @classmethod
    @jwt_required()
    def put(cls, username):
        data = request.get_json()

        if data is None or current_identity is None:
            return {'message': 'insufficient arguments'}, 400

        user = UserContactModel.put_user_contact(username, data)

        if user:
            return {"status": "User contact info created successfully"}, 200
        else:
            return {"status": "Unable to create the user contact info"}, 400
