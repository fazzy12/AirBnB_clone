#!/usr/bin/env python3
"""This module contains the Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel

    Attributes:
        name (str): amenity's name
    """
    name = ""