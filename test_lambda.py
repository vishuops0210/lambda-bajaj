import json
from lambda_function import lambda_handler

def test_lambda_handler(mocker):
    # Mock the requests.get call
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mocker.patch('lambda_function.requests.get', return_value=mock_response)
    
    response = lambda_handler({}, {})
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['message'] == 'Hello from Bajaj Capital Lambda CI/CD!'