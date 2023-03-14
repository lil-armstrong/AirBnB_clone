#!/usr/bin/python3
from models.base_model import BaseModel
"""User model module"""


class User(BaseModel):
    """user class definition
    Represent a user model object
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Instantiate User object"""
        super().__init__(*args, **kwargs)
