import json
import boto3
import unittest

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('dynamo_terraform')

def getCtr():
    ctr = int(table.get_item(
        Key = { 'views': 'views' }
    )['Item']['counter'])
    return ctr

def update():
    table.update_item(
        Key = { 'views': 'views' },
        UpdateExpression = "SET #ct= :s",
        ExpressionAttributeValues = { ':s': getCtr()+1 },
        ExpressionAttributeNames = { "#ct": "counter" },
        ReturnValues = "UPDATED_NEW",
    )
    #hello world asdasdadsads feeetete123test12313211231321
def put14():
    table.put_item(
       Item={
        'views': 'views',
        'counter': 1
       } 
    )
    
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
