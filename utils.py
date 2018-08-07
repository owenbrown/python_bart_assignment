"""Optional helper function """


def get_station_name(event: dict) -> str:
    """Get the station name that a user spoke from the event
    
    Args:
        event (dict): The payload posted from DialogFlow to our endpoint
    
    Returns
        (str): The station name. This corresponds to the "dialog_flow_entity" key in the stations list
    """
    pass


def get_direction(event: dict) -> str:
    """Get the direction of the train that the user spoke.
    
    Args:
        event (dict): The payload posted from DialogFlow to our endpoint
    
    Returns
        (str): Represents cardinal direction that the user spoke
    """
    
    pass
