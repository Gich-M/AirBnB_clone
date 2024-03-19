#!/usr/bin/python3
#!/usr/bin/env python3
#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel

"""
    Defines a place object.

    Attributes:
        city_id (str): The City id of the place.
        user_id (str): The ID of the user.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price of the place per night.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of the Amenity IDs.
"""


class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
