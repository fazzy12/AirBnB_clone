#!/usr/bin/env python3
"""This module contains the BaseModel class"""



import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertIsInstance(model.id, str)

    def test_save_method(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_str_method(self):
        model = BaseModel()
        str_repr = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), str_repr)

    def test_to_dict_method(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertRegex(model_dict['created_at'], r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?$')
        self.assertRegex(model_dict['updated_at'], r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?$')
        self.assertIsInstance(model_dict['id'], str)
        # Add more assertions for other keys as needed


if __name__ == '__main__':
    unittest.main()
