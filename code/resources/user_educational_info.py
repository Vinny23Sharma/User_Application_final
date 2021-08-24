from flask_restful import Resource
from flask import request
from code.model.user_educational_info import UserEducationalInfo


class UserEducationalInfoResource(Resource):
    @classmethod
    def post(cls, username):
        data = request.get_json()
        user = UserEducationalInfo.put_user_educational_info(username, data)

        if user:
            return {"status": "User educational info created successfully"}, 200
        else:
            return {"status": "Unable to create the user educational info"}, 400

    @classmethod
    def get(cls, username):

        try:
            user = UserEducationalInfo.get_user_educational_info(username)
            data = user.get('Item')

            if data.get('TenthSchoolName'):
                return {
                           'TenthSchoolName': data.get('TenthSchoolName'),
                           'TenthBoard': data.get('TenthBoard'),
                           'TenthPercentage': data.get('TenthPercentage'),
                           'TenthPassingYear': data.get('TenthPassingYear'),
                           'TwelfthSchoolName': data.get('TwelfthSchoolName'),
                           'TwelfthBoard': data.get('TwelfthBoard'),
                           'TwelfthPercentage': data.get('TwelfthPercentage'),
                           'TwelfthPassingYear': data.get('TwelfthPassingYear'),
                           'GraduatingUniversityName': data.get('GraduatingUniversityName'),
                           'GraduationPercentage': data.get('GraduationPercentage'),
                           'GraduationPassOutYear': data.get('GraduationPassOutYear')

                       }, 200
            else:
                return {"status": "Unable to get the user educational info"}, 500
        except:
            return {"status": "Unable to get the user educational info"}, 500

    @classmethod
    def put(cls, username):
        data = request.get_json()
        user = UserEducationalInfo.put_user_educational_info(username, data)

        if user:
            return {"status": "User educational info created successfully"}, 200
        else:
            return {"status": "Unable to create the user educational info"}, 400
