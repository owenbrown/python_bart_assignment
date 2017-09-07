"""Bart Helper lambda function code, which is triggered by HTTPS calls from Api.ai to the Api gateway."""
import json
from utils import get_station_name, get_direction


def lambda_handler(event, context):
    """Takes in an event from Api.ai, through Api Gateway.
    Returns a dict with keys "speech", "displayText", and "Source".
    Source is always the "BART API"    """
    return dict()


def test_lambda_handler():
    """This may be helpful when testing your function"""
    with open(file='sample_event.json', mode='r') as f:
        sample_event = json.load(f)

    response = lambda_handler(sample_event, None)
    print(json.dumps(response, indent=4))


if __name__ == '__main__':
    test_lambda_handler()
