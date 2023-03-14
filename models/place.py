#!/usr/bin/python3
from models.base_model import BaseModel
"""Place model module"""


class Place(BaseModel):
    """Place class definition
    Represent a Place model object
    """
    name = ""
    city_id = ""
    user_id = ""
    amenity_id = []
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0

    def __init__(self, *args, **kwargs):
        """Instantiate Place object"""
        super().__init__(*args, **kwargs)
