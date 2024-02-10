#!/usr/bin/env python3
"""Defines the State class."""
from .base_model import BaseModel


class State(BaseModel):
    """
    Defines a state object.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
