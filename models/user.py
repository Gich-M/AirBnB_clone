#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


"""
Represents a User.

Attributes:
    email (str): The email of the user.
    pasword (str): The password of the user.
    first_name (str): The first name of the user.
    last_name (str): The last name of the user.
"""


class User(BaseModel):
    email = ""
    pasword = ""
    first_name = ""
    last_name = ""
