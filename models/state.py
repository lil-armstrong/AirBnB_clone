#!/usr/bin/python3
from models.base_model import BaseModel
"""State model module"""


class State(BaseModel):
    """State class definition
    Represent a state model object
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiate State object"""
        super().__init__(*args, **kwargs)
