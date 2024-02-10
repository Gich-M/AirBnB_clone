#!/usr/bin/env python3
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance

        Args:
            *args (any): A dictionary
            **kwargs (dict): Key/value pairs of attributes
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
        dict: A dictionary containing the attribute values of the object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = str(self.created_at.isoformat())
        obj_dict['updated_at'] = str(self.updated_at.isoformat())
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict

    def save(self):
        """
        Saves the object by updating the `updated_at`
                attribute to the current datetime.

        Returns:
        None
        """
        from . import storage
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
        str: A string representation of the object.
        """
        return "[{}] [{}] [{}])".format(self.__class__.__name__,
                                        self.id, self.__dict__)
