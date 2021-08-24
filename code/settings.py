import boto3

# this is for local host
# dynamodb_connector = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
dynamodb_connector = boto3.resource('dynamodb')
user_table_instance = dynamodb_connector.Table('users')

