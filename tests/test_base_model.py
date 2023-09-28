#!/usr/bin/env python3
"""Unittest for BaseModel class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        # Test if id is a string
        model = BaseModel()
        self.assertIsInstance(model.id, str)

        # Test if created_at and updated_at are datetime objects
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_method(self):
        # Test the __str__() method
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

    def test_save_method(self):
        # Test the save() method
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

    def test_to_dict_method(self):
        # Test the to_dict() method
        model = BaseModel()
        model_dict = model.to_dict()

        # Check if '__class__' is in the dictionary
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

        # Check if 'id', 'created_at', and 'updated_at' are in the dictionary
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

        # Check if 'id', 'created_at', and 'updated_at' are in ISO format
        self.assertRegex(model_dict['id'], r'^[0-9a-f-]+$')
        self.assertRegex(model_dict['created_at'], r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?$')
        self.assertRegex(model_dict['updated_at'], r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?$')

if __name__ == '__main__':
    unittest.main()
