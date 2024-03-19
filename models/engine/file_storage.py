#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from hashlib import md5


class FileStorage:
    """Represents a storage engine.

    Attributes:
        __file_path (str): The name of the file to save to.
        __objects (str): A dictionary of instatiated objects.
        """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for obj in objdict.values():
                    clsname = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(clsname)(**obj))
        except FileNotFoundError:
            return
