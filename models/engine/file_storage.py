#!/usr/bin/env python3
"""This module contains the FileStorage class and its methods for the models"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file.

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): empty but will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects

        Returns:
            dict: __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Args:
            obj (BaseModel): object to be set
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, mode="w") as file:
            dict_storage = {}
            for key, value in self.__objects.items():
                dict_storage[key] = value.to_dict()
            json.dump(dict_storage, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn't
        exist, no exception should be raised)

        Returns:
            None

        Raises:
            FileNotFoundError: if the JSON file doesn't exist
        """
        try:
            with open(self.__file_path, encoding="utf-8") as file:
                for obj_data in json.load(file).values():
                    class_name = obj_data["__class__"]

                    # Create instances based on class_name
                    if class_name == "BaseModel":
                        obj = BaseModel(**obj_data)
                    elif class_name == "User":
                        obj = User(**obj_data)
                    else:
                        # Handle other classes as needed
                        continue

                    self.new(obj)
        except FileNotFoundError:
            return
