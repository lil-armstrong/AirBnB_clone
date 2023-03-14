#!/usr/bin/python3
from models.base_model import BaseModel
"""Amenity model module"""


class Amenity(BaseModel):
    """Amenity class definition
    Represent a Amenity model object
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiate Amenity object"""
        super().__init__(*args, **kwargs)
