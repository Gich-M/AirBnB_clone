#!/usr/bin/env python3
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
            with open(FileStorage.__file_path) as f:
                if os.stat(FileStorage.__file_path).st_size != 0:
                    data = json.load(f)
                    for key in data.values():
                        cls_name = key["__class__"]
                        del key["__class__"]
                        self.new(eval(cls_name)(**key))
        except FileNotFoundError:
            return
