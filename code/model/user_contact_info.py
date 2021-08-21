import boto3


# Get the service resource.

class UserContactModel:
    dynamodb_connector = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    user_table_instance = dynamodb_connector.Table('users')

    @classmethod
    def put_user_contact(cls, username, data):
        user = cls.user_table_instance.update_item(
            Key={
                "username": username,
            },
            UpdateExpression="""set Mobile_No_1=:m1, Mobile_No_2=:m2, Landline=:l, Company_email_address=:e1, 
                                                 Personal_email_address=:pe, Work_address=:wa, Emergency_contact_1:=ec1,
                                                 Emergency_contact_2:=ec2, Current_address:=ca, Permanent_address:=pa
                                                 """,
            ExpressionAttributeValues={
                ':m1': data['Mobile_No_1'],
                ':m2': data['Mobile_No_2'],
                ':l': data['Landline'],
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

        return user

    @classmethod
    def get_user_contact(cls, username):
        user = cls.user_table_instance.get_item(
            Key={
                'username': username,
            }
        )

        return user
