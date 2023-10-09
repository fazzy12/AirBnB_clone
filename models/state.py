#!/usr/bin/env python3
"""This module contains the State class"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel

    Attributes:
        name (str): state's name
    """
    name = ""