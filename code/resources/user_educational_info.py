from flask_restful import Resource, reqparse
from code.model.user_educational_info import UserEducationalInfo


class UserEducationalInfoResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('TenthSchoolName',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('TenthBoard',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('TenthPercentage',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('TenthPassingYear',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('TwelfthSchoolName',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('TwelfthBoard',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('TwelfthPercentage',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('TwelfthPassingYear',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('GraduatingUniversityName',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('GraduationPercentage',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('GraduationPassOutYear',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )

    @classmethod
    def post(cls, username):
        data = cls.parser.parse_args()
        user = UserEducationalInfo.put_user_educational_info(username, data)

        if user:
            return {"status": "User contact info created successfully"}, 200
        else:
            return {"status": "Unable to create the user contact info"}, 400

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
                return {"status": "Unable to get the user contact info"}, 500
        except:
            return {"status": "Unable to get the user contact info"}, 500

    @classmethod
    def put(cls, username):
        data = cls.parser.parse_args()
        user = UserEducationalInfo.put_user_educational_info(username, data)

        if user:
            return {"status": "User contact info created successfully"}, 200
        else:
            return {"status": "Unable to create the user contact info"}, 400
