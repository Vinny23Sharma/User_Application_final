from flask_restful import Resource
from code.model.user_educational_info import UserEducationalInfo
from code.resources.helperfile import UserEducationalInfoRequestParser


class UserEducationalInfoResource(Resource):

    @classmethod
    def post(cls, username):
        data = UserEducationalInfoRequestParser.get_user_educational_info_request_parser().parse_args()
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
                return UserEducationalInfoRequestParser.get_user_educational_info_response(data)
            else:
                return {"status": "Unable to get the user contact info"}, 500
        except:
            return {"status": "Unable to get the user contact info"}, 500

    @classmethod
    def put(cls, username):
        data = UserEducationalInfoRequestParser.get_user_educational_info_request_parser().parse_args()
        user = UserEducationalInfo.put_user_educational_info(username, data)

        if user:
            return {"status": "User contact info created successfully"}, 200
        else:
            return {"status": "Unable to create the user contact info"}, 400
