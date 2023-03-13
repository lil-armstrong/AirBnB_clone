#!/usr/bin/python3
import os
import json
from models.base_model import BaseModel
from uuid import uuid4

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

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized = {}
        objects = self.all()
        for k, v in FileStorage.__objects.items():
            serialized[k] = v.to_dict()

        with open(self.filePath, "w") as fp:
            if (len(objects) == 0):
                fp.write("[]")
            else:
                json.dump(serialized, fp)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.filePath):
            with open(self.filePath, "r") as fp:
                # deserialize json file to __objects
                serialized = json.load(fp)

                for v in serialized.values():
                    cls_name = v["__class__"]
                    self.new(eval(cls_name)(**v))
