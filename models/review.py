#!/usr/bin/python3
from models.base_model import BaseModel
"""Review model module"""


class Review(BaseModel):
    """Review class definition
    Represent a Review model object
    """
    text = ""
    place_id = ""
    user_id = ""

    def __init__(self, *args, **kwargs):
        """Instantiate Review object"""
        super().__init__(*args, **kwargs)
