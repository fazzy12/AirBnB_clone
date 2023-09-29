#!/usr/bin/env python3
"""This module contains the BaseModel class and its methods for the models"""

import uuid
from datetime import datetime

class BaseModel:
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)"""
    def __init__(self):
        """Initialize the instance attributes

        Args:
            id (str): unique id of the instance
            created_at (datetime): creation date of the instance
            updated_at (datetime): update date of the instance

        Attributes:
            id (str): unique id of the instance
            created_at (datetime): creation date of the instance
            updated_at (datetime): update date of the instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the instance

        Returns:
            str: string representation of the instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the public instance attribute updated_at with the current
        datetime

        Returns:
            None
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of
        __dict__ of the instance

        Returns:
            dict: dictionary containing all keys/values of __dict__
            of the instance

        Notes:
            The dictionary returned by to_dict() must contain:
                - __class__: the class name of the object
                - created_at: string representing the date of creation
                of the object in the format YYYY-MM-DDTHH:MM:SS.mmmmmm
                - updated_at: string representing the date of update
                of the object in the format YYYY-MM-DDTHH:MM:SS.mmmmmm
        """
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
