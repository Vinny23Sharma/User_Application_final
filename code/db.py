import boto3


def create_table():
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    # Create the DynamoDB table.
    try:
        dynamodb.create_table(
            TableName='users',
            KeySchema=[
                {
                    'AttributeName': 'username',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'username',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

    except dynamodb.exceptions.ResourceInUseException:
        print("Table Exists")
        pass
