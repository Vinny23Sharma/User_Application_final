from flask_restful import Resource
from code.model.user_personal_info import UserPersonalInfo
from code.resources.helperfile import UserPersonalInfoRequestParser


class UserPersonalInfoResource(Resource):

    @classmethod
    def post(cls, username):
        data = UserPersonalInfoRequestParser.get_user_personal_info_request_parser().parse_args()
        user = UserPersonalInfo.put_user_personal_info(username, data)

        if user:
            return {"status": "User contact info created successfully"}, 200
        else:
            return {"status": "Unable to create the user contact info"}, 400

    @classmethod
    def get(cls, username):
        try:
            user = UserPersonalInfo.get_user_personal_info(username)
            data = user.get('Item')

            if data.get('TenthSchoolName'):
                return UserPersonalInfoRequestParser.get_user_personal_info_response(data)
            else:
                return {"status": "Unable to get the user contact info"}, 500
        except:
            return {"status": "Unable to get the user contact info"}, 500

    @classmethod
    def put(cls, username):
        data = UserPersonalInfoRequestParser.get_user_personal_info_request_parser().parse_args()
        user = UserPersonalInfo.put_user_personal_info(username, data)

        if user:
            return {"status": "User contact info created successfully"}, 200
        else:
            return {"status": "Unable to create the user contact info"}, 400
