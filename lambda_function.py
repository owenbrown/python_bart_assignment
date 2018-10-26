"""Bart Helper lambda function code, which is triggered by HTTPS calls from Api.ai to the Api gateway."""
import json
from utils import get_station_name, get_direction


def lambda_handler(event: dict, context) -> dict:
    """Takes in an event from AWS API Gateway. 
    The event is the payload of the POST request made from DialogFlow to the our fulfillment endpoint.
    Use the included sample_event.json, which should match this format:
    https://developers.google.com/actions/reference/v1/dialogflow-webhook#request

    The lambda function returns a dict that should match this format:
    https://developers.google.com/actions/build/json/dialogflow-webhook-json#dialogflow-response-body
    Source is always the "BART API"    """
    pass


def test_lambda_handler():
    """This may be helpful when testing your function"""
    with open(file='sample_event.json', mode='r') as f:
        sample_event = json.load(f)

    response = lambda_handler(sample_event, None)
    print(json.dumps(response, indent=4))


if __name__ == '__main__':
    test_lambda_handler()
