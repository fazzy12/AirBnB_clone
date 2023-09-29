#!/usr/bin/env python3
"""This module contains the BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_attributes(self):
        """Test attributes of BaseModel class"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertIsInstance(model.id, str)

    def test_save_method(self):
        """Test save method of BaseModel class"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_str_method(self):
        """Test str method of BaseModel class"""
        model = BaseModel()
        str_repr = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), str_repr)

    def test_to_dict_method(self):
        """Test to_dict method of BaseModel class"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertRegex(model_dict['created_at'],
                         r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?$')
        self.assertRegex(model_dict['updated_at'],
                         r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?$')
        self.assertIsInstance(model_dict['id'], str)

    def test_instance_equality(self):
        """Test instance equality of BaseModel class"""
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertFalse(my_model is my_new_model)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.created_at, my_new_model.created_at)


if __name__ == '__main__':
    unittest.main()
