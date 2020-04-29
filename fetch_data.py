import boto3
from settings import os


dynamodb = boto3.resource(os.getenv('RESOURCE'),
                          aws_access_key_id=os.getenv('ACCESS_KEY'),
                          aws_secret_access_key=os.getenv('SECRET'),
                          region_name=os.getenv('REGION'),
                         )

try:
    table = dynamodb.Table('users')
    response = table.scan()
    items = response['Items']
    print(items)

except Exception as e:
    print(e)



#aws_session_token=aws_session_token,
#                          aws_access_key_id=aws_access_key_id,
#                          aws_secret_access_key=aws_secret_access_key,
#                         region_name=region