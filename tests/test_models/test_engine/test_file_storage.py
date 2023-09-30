#!/usr/bin/python3
"""Unittest for FileStorage class"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.base_model = BaseModel()
        self.base_model.name = "Test Model"
        self.base_model.my_number = 42

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_empty(self):
        all_objects = self.storage.all()

    def test_new_and_all(self):
        self.storage.new(self.base_model)
        all_objects = self.storage.all()
        key = "BaseModel.{}".format(self.base_model.id)
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key], self.base_model)

    def test_save_and_reload(self):
        self.storage.new(self.base_model)
        self.storage.save()

        # Create a new storage instance to simulate program restart
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        all_objects = new_storage.all()
        key = "BaseModel.{}".format(self.base_model.id)
        self.assertIn(key, all_objects)
        reloaded_model = all_objects[key]
        self.assertIsInstance(reloaded_model, BaseModel)
        self.assertEqual(reloaded_model.id, self.base_model.id)
        self.assertEqual(reloaded_model.name, self.base_model.name)
        self.assertEqual(reloaded_model.my_number, self.base_model.my_number)

if __name__ == '__main__':
    unittest.main()
