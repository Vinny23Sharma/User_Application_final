from flask_restful import Resource, reqparse
from flask import request
from code.model.user_personal_info import UserPersonalInfo


class UserPersonalInfoResource(Resource):
    @classmethod
    def post(cls, username):
        data = request.get_json()
        print(data)
        user = UserPersonalInfo.put_user_personal_info(username, data)

        if user:
            return {"status": "User personal info created successfully"}, 200
        else:
            return {"status": "Unable to create the user personal info"}, 400

    @classmethod
    def get(cls, username):
        try:
            user = UserPersonalInfo.get_user_personal_info(username)
            data = user.get('Item')

            if data.get('TenthSchoolName'):
                return {
                           'FirstName': data.get('FirstName'),
                           'LastName': data.get('LastName'),
                           'MotherName': data.get('MotherName'),
                           'FatherName': data.get('FatherName'),
                           'DateOfBirth': data.get('DateOfBirth'),
                           'Gender': data.get('Gender'),
                           'BloodGroup': data.get('BloodGroup'),
                           'MaritalStatus': data.get('MaritalStatus'),
                           'Occupation': data.get('Occupation'),
                           'Nationality': data.get('Nationality')
                       }, 200

            else:
                return {"status": "Unable to get the user personal info"}, 500
        except:
            return {"status": "Unable to get the user personal info"}, 500

    @classmethod
    def put(cls, username):
        data = request.get_json()
        user = UserPersonalInfo.put_user_personal_info(username, data)

        if user:
            return {"status": "User personal info created successfully"}, 200
        else:
            return {"status": "Unable to create the user personal info"}, 400
