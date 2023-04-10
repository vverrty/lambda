import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('dynamo_terraform')

#Get counter
def getCtr():
    ctr = int(table.get_item(
        Key = { 'views': 'views' }
    )['Item']['counter'])
    return ctr
#update the counter value +1
def update():
    table.update_item(
        Key = { 'views': 'views' },
        UpdateExpression = "SET #ct= :s",
        ExpressionAttributeValues = { ':s': getCtr()+1 },
        ExpressionAttributeNames = { "#ct": "counter" },
        ReturnValues = "UPDATED_NEW",
    )

#initillay I used the unittest library to test whether DynamoDB would actually make changes
futureCounter = getCtr() + 1

def lambda_handler(event, context):
    update()
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST'
        },
        "body": json.dumps({
            "count": getCtr()
        })
    }
