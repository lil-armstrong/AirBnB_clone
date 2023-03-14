#!/usr/bin/python3
import os
import json
from models import base_model
from models import user
from models import amenity
from models import city
from models import place
from models import review
from models import state

BaseModel = base_model.BaseModel
User = user.User
Amenity = amenity.Amenity
City = city.City
Place = place.Place
Review = review.Review
State = state.State
"""FileStorage serializes class instances to a JSON file
and deserializes JSON file to instances"""


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    @property
    def filePath(self):
        """Return the file path"""
        return FileStorage.__file_path

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        key = FileStorage.makeKey(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def remove(self, key):
        """Removes a key from the __objects"""
        # Checks if the key exist
        objs = FileStorage.__objects
        if key in objs:
            del objs[key]

        return objs

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(self.filePath, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.filePath):
            with open(self.filePath, "r") as fp:
                # deserialize json file to __objects
                serialized = json.load(fp)

                for v in serialized.values():
                    cls_name = v["__class__"]
                    self.new(eval(cls_name)(**v))

    @staticmethod
    def makeKey(cls_name, id):
        """Generates a storage key using the class name and id"""
        return "{}.{}".format(cls_name, id)
