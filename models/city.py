#!/usr/bin/env python3
"""This module contains the City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel

    Attributes:
        state_id (str): state's id
        name (str): city's name
    """
    state_id = ""
    name = ""
