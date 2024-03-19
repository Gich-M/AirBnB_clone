#!/usr/bin/python3
#!/usr/bin/env python3
#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class defines the Review model.

    Attributes:
        place_id (str): The unique identifier of the place.
        user_id (str): The unique identifier of the user.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
