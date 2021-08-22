import boto3
from code.model.settings import UserEducationalInfoHelper


class UserEducationalInfo:
    dynamodb_connector = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    user_table_instance = dynamodb_connector.Table('users')

    @classmethod
    def put_user_educational_info(cls, username, data):
        user = cls.user_table_instance.update_item(
            Key=UserEducationalInfoHelper.get_key(username),
            UpdateExpression=UserEducationalInfoHelper.get_update_expression(),
            ExpressionAttributeValues=UserEducationalInfoHelper.get_expression_attribute_values(data),
            ReturnValues="UPDATED_NEW"
        )
        return user

    @classmethod
    def get_user_educational_info(cls, username):
        user = cls.user_table_instance.get_item(
            Key=UserEducationalInfoHelper.get_key(username)
        )

        return user
