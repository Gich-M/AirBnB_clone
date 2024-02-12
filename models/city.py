#!/usr/bin/env python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class defines a city object.

    Attributes:
        state_id (str): The state id of the city.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
