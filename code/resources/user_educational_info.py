from flask_restful import Resource
from flask import request
from code.model.user_educational_info import UserEducationalInfo
from flask_jwt import current_identity, jwt_required


class UserEducationalInfoResource(Resource):
    @classmethod
    @jwt_required()
    def post(cls, username):
        data = request.get_json()

        if data is None or current_identity is None:
            return {'message': 'insufficient arguments'}, 400

        user = UserEducationalInfo.put_user_educational_info(username, data)

        if user:
            return {"status": "User educational info created successfully"}, 200
        else:
            return {"status": "Unable to create the user educational info"}, 400

    @classmethod
    @jwt_required()
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
    @jwt_required()
    def put(cls, username):
        data = request.get_json()
        user = UserEducationalInfo.put_user_educational_info(username, data)

        if user:
            return {"status": "User educational info created successfully"}, 200
        else:
            return {"status": "Unable to create the user educational info"}, 400
