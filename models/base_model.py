#!/usr/bin/python3
import models 
from uuid import uuid4
from datetime import datetime

"""Base Model"""


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes the base class instance"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if (len(kwargs) != 0):
            for k, v in kwargs.items():
                if k != "__class__":
                    if (k in ["created_at", "updated_at"]):
                        v = datetime.fromisoformat(v)
                    self.__dict__[k] = v

        else:
            models.storage.new(self)

    def __str__(self):
        """Return string representation of the Base class"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)

    def save(self):
        """Save the instance object"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        dict_obj = self.__dict__
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()
        return dict_obj
