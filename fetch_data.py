from dynamodb_conn import dynamodb

try:
    table = dynamodb.Table('users')
    response = table.scan()
    items = response['Items']
    print(items)

except Exception as e:
    print(e)