def lambda_handler(event, context):
    """Takes in an event from Api.ai, through Api Gateway.
    Returns a dict with keys "speech", "displayText", and "Source".
    Source is always the "BART Api".  """
    