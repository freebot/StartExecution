import json
import urllib.parse
import boto3
import uuid

client = boto3.client('stepfunctions')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
   
    # Get the object from the event and show its content type
    #bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], 
encoding='utf-8')
    unique_sf_identifier = str(uuid.uuid1())
    input = { "key" : key }
    
    response = client.start_execution(
        stateMachineArn = '',
        name = unique_sf_identifier,
        input = json.dumps(input)
        )
   
