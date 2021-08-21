from flask_restful import Resource, reqparse
import boto3

from code.model import user_educational_info
dynamodb_connector = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
user_table_instance = dynamodb_connector.Table('users')


"""
1.	Mobile_No_1 :Number
2.	Mobile_No_2:Number
3.	Landline :Number
4.	Personal_email_address: String
5.	Company_email_address: String
6.	Permanent_address: String
7.	Current_address: String
8.	Work_address: String
9.	Emergency_contact_1: Number
10.	Emergency_contact_2:Number
"""


# To get, post and put the user's educational information
class User_educational_info(Resource):
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
    def search_by_username(self, name):
        pass

    def post(self, username):
        data = User_educational_info.parser.parse_args()
        response = user_table_instance.update_item(
            Key={
                "username": username,
            },
            UpdateExpression="""set Mobile_No_1=:m1, Mobile_No_2=:m2, Landline=:l, Company_email_address=:e1, 
                             Personal_email_address=:pe, Work_address=:wa, Emergency_contact_1:=ec1,
                             Emergency_contact_2:=ec2, Current_address:=ca, Permanent_address:=pa
                             """
                             ,
            ExpressionAttributeValues={
                ':m1': data['Mobile_No_1'],
                ':m2': data['Mobile_No_2'],
                ':l':  data['Landline'],
                ':e1': data['Company_email_address'],
                ':pe': data['Personal_email_address'],
                ':wa': data['Work_address'],
                ':ec1': data['Emergency_contact_1'],
                ':ec2': data['Emergency_contact_2'],
                ':ca': data['Current_address'],
                ':pa': data['Permanent_address']
            },
            ReturnValues="UPDATED_NEW"
        )
        return response





    def get(self, username):
        pass

    def put(self, username):
        pass



