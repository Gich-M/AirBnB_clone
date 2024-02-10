#!/usr/bin/env python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import amenity


class FileStorage:
    """
    Defines the FileStorage class.
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
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file __file_path.
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({key: value.to_dict() for key,
                       value in FileStorage.__objects.items()}, f)

    def reload(self):
        """
        Deserializes __objects from the JSON file __file_path.
        """
        try:
            if os.path.getsize(self.__file_path) > 0:
                with open(FileStorage.__file_path, 'r') as f:
                    data = json.load(f)
                    for key, value in data.items():
                        obj = BaseModel(**value)
                        FileStorage.__objects[key] = obj.to_dict()
            else:
                FileStorage.__objects = {}
        except FileNotFoundError:
            return FileStorage.__objects
