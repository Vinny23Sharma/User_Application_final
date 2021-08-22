import boto3

dynamodb_connector = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
user_table_instance = dynamodb_connector.Table('users')

