from flask_restful import Resource, reqparse
from code.model.user_contact_info import UserContactModel


class User_contact_info(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Mobile_No_1',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('Mobile_No_2',
                        type=int,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('Landline',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('Company_email_address',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('Personal_email_address',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('Permanent_address',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('Current_address',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('Work_address',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('Emergency_contact_1',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('Emergency_contact_2',
                        type=int,
                        required=True,
                        help="This field cannot be left blank"
                        )

    @classmethod
    def post(cls, username):
        data = cls.parser.parse_args()
        user = UserContactModel.put_user_contact(username, data)

        if user:
            return {"status": "User contact info created successfully"}, 200
        else:
            return {"status": "Unable to create the user contact info"}, 400

    @classmethod
    def get(cls, username):
        try:
            user = UserContactModel.get_user_contact(username)
            data = user.get('Item')

            if data.get('Personal_email_address') != 'NULL':
                return {
                           'Mobile_No_1': data['Mobile_No_1'],
                           'Mobile_No_2': data['Mobile_No_2'],
                           'Landline': data['Landline'],
                           'Company_email_address': data['Company_email_address'],
                           'Personal_email_address': data['Personal_email_address'],
                           'Work_address': data['Work_address'],
                           'Emergency_contact_1': data['Emergency_contact_1'],
                           ':Emergency_contact_2': data['Emergency_contact_2'],
                           'Current_address': data['Current_address'],
                           'Permanent_address': data['Permanent_address']
                       }, 200
            else:
                return {"status": "Unable to get the user contact info"}, 500
        except:
            return {"status": "Unable to get the user contact info"}, 500

    @classmethod
    def put(cls, username):
        data = cls.parser.parse_args()
        user = UserContactModel.put_user_contact(username, data)

        if user:
            return {"status": "User contact info created successfully"}, 200
        else:
            return {"status": "Unable to create the user contact info"}, 400
