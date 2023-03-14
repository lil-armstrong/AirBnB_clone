#!/usr/bin/python3
from models.engine.file_storage import FileStorage
"""__init__ magic method for models directory"""


storage = FileStorage()
storage.reload()

__all__ = ["base_model", "console", "storage",
           "user", "amenity", "city", "place", "state", "review"]
