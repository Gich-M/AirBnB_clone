#!/usr/bin/env python3
"""Defines the Review class."""
from .base_model import BaseModel

"""
This class defines the Review model.

Attributes:
    place_id (str): The unique identifier of the place.
    user_id (str): The unique identifier of the user.
    text (str): The text of the review.
"""


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
