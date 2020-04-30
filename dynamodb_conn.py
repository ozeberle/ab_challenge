import boto3
from settings import os


dynamodb = boto3.resource(os.getenv('RESOURCE'),
                          aws_access_key_id=os.getenv('ACCESS_KEY'),
                          aws_secret_access_key=os.getenv('SECRET'),
                          region_name=os.getenv('REGION'),
                         )
