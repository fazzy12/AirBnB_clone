#!/usr/bin/env python3
"""This module contains the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel

    Attributes:
        place_id (str): place's id
        user_id (str): user's id
        text (str): review's text
    """
    place_id = ""
    user_id = ""
    text = ""
