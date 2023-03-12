#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

"""Base Model"""


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initializes the base class instance"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """Return string representation of the Base class"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)

    def save(self):
        """Save the instance object"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        dict_obj = self.__dict__
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj.update({"created_at": str(self.created_at),
                        "updated_at": str(self.updated_at)})
        return dict_obj
