import json
import boto3

print('Loading function')


def handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    return "hello, world"
