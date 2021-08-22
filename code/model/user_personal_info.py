import boto3
from code.model.settings import UserPersonalInfoHelper


class UserPersonalInfo:
    dynamodb_connector = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    user_table_instance = dynamodb_connector.Table('users')

    @classmethod
    def put_user_personal_info(cls, username, data):
        user = cls.user_table_instance.update_item(
            Key=UserPersonalInfoHelper.get_key(username),
            UpdateExpression=UserPersonalInfoHelper.get_update_expression(),
            ExpressionAttributeValues=UserPersonalInfoHelper.get_expression_attribute_values(data),
            ReturnValues="UPDATED_NEW"
        )
        return user

    @classmethod
    def get_user_personal_info(cls, username):
        user = cls.user_table_instance.get_item(
            Key=UserPersonalInfoHelper.get_key(username)
        )

        return user
