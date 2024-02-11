#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """
    Represent a storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instanciated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """"
        Adds new objects __objects obj with key <obj_class_name>.id
        """
        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file __file_path.
        """
        o_dict = FileStorage.__objects
        objdict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(objdict, f)

    def reload(self):
        """
        Deserializes __objects from the JSON file __file_path.
        """
        try:
            with open(FileStorage.__file_path) as f:
                    data = json.load(f)
                    for key in data.values():
                        cls_name = key["__class__"]
                        del key["__class__"]
                        self.new(eval(cls_name)(**key))
        except FileNotFoundError:
            return
