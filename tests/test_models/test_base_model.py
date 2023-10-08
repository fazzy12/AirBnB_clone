#!/usr/bin/env python3
"""Unittest for BaseModel class"""

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import json
import os


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        # Create a clean storage instance before each test
        storage.reload()

    def tearDown(self):
        # Clean up any created files
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_new_instance_has_id_created_at_updated_at(self):
        """Test that a new instance has 'id', 'created_at',
        and 'updated_at' attributes."""
        bm = BaseModel()
        self.assertTrue(hasattr(bm, 'id'))
        self.assertTrue(hasattr(bm, 'created_at'))
        self.assertTrue(hasattr(bm, 'updated_at'))

    def test_id_is_string(self):
        """Test that 'id' attribute is a string."""
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_created_at_and_updated_at_are_datetimes(self):
        """Test that 'created_at' and 'updated_at' attributes
        are instances of datetime."""
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Test that the 'save' method updates the 'updated_at' attribute."""
        bm = BaseModel()
        initial_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(initial_updated_at, bm.updated_at)

    def test_to_dict_returns_dict_with_expected_keys(self):
        """Test that 'to_dict' method returns a dictionary
        with expected keys."""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertCountEqual(bm_dict.keys(), expected_keys)

    def test_to_dict_returns_dict_with_custom_attributes(self):
        """Test that 'to_dict' method includes custom attributes."""
        bm = BaseModel()
        bm.name = "TestModel"
        bm.my_number = 42
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict['name'], "TestModel")
        self.assertEqual(bm_dict['my_number'], 42)

    def test_save_updates_file(self):
        """Test that the 'save' method updates the storage file."""
        bm = BaseModel()
        bm.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as f:
            data = json.load(f)
            bm_key = f"BaseModel.{bm.id}"
            self.assertIn(bm_key, data)

    def test_reload_loads_objects(self):
        """Test that the 'reload' method loads objects into storage."""
        bm = BaseModel()
        bm.save()
        initial_objects = storage.all()
        # Simulate reloading
        storage.reload()
        reloaded_objects = storage.all()
        self.assertEqual(initial_objects, reloaded_objects)

    def test_str_representation(self):
        """Test the string representation of the object."""
        bm = BaseModel()
        expected_str = f"[BaseModel] ({bm.id}) {{'id': '{bm.id}', \
            'created_at': {repr(bm.created_at)},\
            'updated_at': {repr(bm.updated_at)}}}"

        # Check if the expected substrings are present in the generated string
        self.assertIn(f"[BaseModel] ({bm.id})", str(bm))
        self.assertIn(f"'id': '{bm.id}'", str(bm))
        self.assertIn(f"'created_at': {repr(bm.created_at)}", str(bm))
        self.assertIn(f"'updated_at': {repr(bm.updated_at)}", str(bm))


if __name__ == '__main__':
    unittest.main()
