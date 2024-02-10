#!/usr/bin/env python3
"""Defines the Amenity class."""
from .base_model import BaseModel

"""
Represents an amenity.

Attributes:
    name (str): The name of the amenity.
"""


class Amenity(BaseModel):
    name = ""
