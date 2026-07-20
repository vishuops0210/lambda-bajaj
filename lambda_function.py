import json
import requests

def lambda_handler(event, context):
    response = requests.get("https://api.github.com")
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from Bajaj Capital Lambda CI/CD!',
            'github_status': response.status_code
        })
    }
# this is done testing for bothe the apps.
