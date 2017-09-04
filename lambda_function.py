"""Bart Helper lambda function code, which is triggered by HTTPS calls from Api.ai to the Api gateway."""
import json


def lambda_handler(event, context):
    """Takes in an event from Api.ai, through Api Gateway.
    Returns a dict with keys "speech", "displayText", and "Source".
    Source is always the "BART API"    """
    sample_response = {
        "speech": "The next northbound train leaves sixteenth street mission station in 4 minutes. "
                  "Then, another northbound train will depart embarcedro station in 12 minutes",
        "display API": "The next northbound train leaves 16th St. Mission station in 4 minutes. "
                       "Then, another northbound train will depart 16th St. Mission station in 12 minutes",
        "source": "BART API"
    }
    return sample_response


def test_lambda_handler():
    """This may be helpful when testing your function"""
    with open(file='sample_event.json', mode='r') as f:
        event = json.load(f)
    print(json.dumps(event, indent=4))

    res = lambda_handler(event=event, context=None)
    print(res)
