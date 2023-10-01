#!/usr/bin/env python3
"""This module contains the BaseModel class and its methods for the models"""

import uuid
from models import storage
from datetime import datetime
import json


class BaseModel:
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)"""
    def __init__(self, *args, **kwargs):
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

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

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
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

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
        model_dict = {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }

        # Check if attributes exist before adding them to the dictionary
        if hasattr(self, 'name') and self.name is not None:
            model_dict['name'] = self.name
        if hasattr(self, 'my_number') and self.my_number is not None:
            model_dict['my_number'] = self.my_number

        model_dict['__class__'] = self.__class__.__name__
        return model_dict
