#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_create(self):
        """Unittests for testing create from the HBNB command interpreter."""
        @classmethod
        def setUp(self):
            try:
                os.rename("file.json", "tmp")
            except IOError:
                pass
            FileStorage.__objects = {}

        @classmethod
        def tearDown(self):
            try:
                os.remove("file.json")
            except IOError:
                pass
            try:
                os.rename("tmp", "file.json")
            except IOError:
                pass

            correct = "** class name missing **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create"))
                self.assertEqual(correct, output.getvalue().strip())

            # Test that command execution works properly
            correct = "** class doesn't exist **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create MyModel"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "*** Unknown syntax: MyModel.create()"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
                self.assertEqual(correct, output.getvalue().strip())
            correct = "*** Unknown syntax: BaseModel.create()"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
                self.assertLess(0, len(output.getvalue().strip()))
                testKey = "BaseModel.{}".format(output.getvalue().strip())
                self.assertIn(testKey, storage.all().keys())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create User"))
                self.assertLess(0, len(output.getvalue().strip()))
                testKey = "User.{}".format(output.getvalue().strip())
                self.assertIn(testKey, storage.all().keys())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create State"))
                self.assertLess(0, len(output.getvalue().strip()))
                testKey = "State.{}".format(output.getvalue().strip())
                self.assertIn(testKey, storage.all().keys())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create City"))
                self.assertLess(0, len(output.getvalue().strip()))
                testKey = "City.{}".format(output.getvalue().strip())
                self.assertIn(testKey, storage.all().keys())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Amenity"))
                self.assertLess(0, len(output.getvalue().strip()))
                testKey = "Amenity.{}".format(output.getvalue().strip())
                self.assertIn(testKey, storage.all().keys())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Place"))
                self.assertLess(0, len(output.getvalue().strip()))
                testKey = "Place.{}".format(output.getvalue().strip())
                self.assertIn(testKey, storage.all().keys())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Review"))
                self.assertLess(0, len(output.getvalue().strip()))
                testKey = "Review.{}".format(output.getvalue().strip())
                self.assertIn(testKey, storage.all().keys())

    def test_show(self):
        """Unittests for testing show from the HBNB command interpreter"""

        @classmethod
        def setUp(self):
            try:
                os.rename("file.json", "tmp")
            except IOError:
                pass
            FileStorage.__objects = {}

        @classmethod
        def tearDown(self):
            try:
                os.remove("file.json")
            except IOError:
                pass
            try:
                os.rename("tmp", "file.json")
            except IOError:
                pass

            correct = "** class name missing **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(".show()"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** class doesn't exist **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show MyModel"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("MyModel.show()"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** instance id missing **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show User"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show State"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show City"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show Amenity"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show Place"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show Review"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** instance id missing **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("BaseModel.show()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("User.show()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("State.show()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("City.show()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Amenity.show()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Place.show()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Review.show()"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** no instance found **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show BaseModel 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show User 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show State 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show City 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show Amenity 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show Place 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show Review 1"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** no instance found **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("BaseModel.show(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("User.show(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("State.show(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("City.show(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Amenity.show(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Place.show(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Review.show(1)"))
                self.assertEqual(correct, output.getvalue().strip())

            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["BaseModel.{}".format(testID)]
                command = "show BaseModel {}".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(obj.__str__(), output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create User"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["User.{}".format(testID)]
                command = "show User {}".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(obj.__str__(), output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create State"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["State.{}".format(testID)]
                command = "show State {}".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(obj.__str__(), output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Place"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["Place.{}".format(testID)]
                command = "show Place {}".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(obj.__str__(), output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create City"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["City.{}".format(testID)]
                command = "show City {}".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(obj.__str__(), output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Amenity"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["Amenity.{}".format(testID)]
                command = "show Amenity {}".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(obj.__str__(), output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Review"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["Review.{}".format(testID)]
                command = "show Review {}".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(obj.__str__(), output.getvalue().strip())

            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["BaseModel.{}".format(testID)]
                command = "BaseModel.show({})".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(obj.__str__(), output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create User"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["User.{}".format(testID)]
                command = "User.show({})".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(obj.__str__(), output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create State"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["State.{}".format(testID)]
                command = "State.show({})".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(obj.__str__(), output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Place"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["Place.{}".format(testID)]
                command = "Place.show({})".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(obj.__str__(), output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create City"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["City.{}".format(testID)]
                command = "City.show({})".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(obj.__str__(), output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Amenity"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["Amenity.{}".format(testID)]
                command = "Amenity.show({})".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(obj.__str__(), output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Review"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["Review.{}".format(testID)]
                command = "Review.show({})".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(obj.__str__(), output.getvalue().strip())

    def test_destroy(self):
        """Unittests for testing destroy from the HBNB command interpreter."""

        @classmethod
        def setUp(self):
            try:
                os.rename("file.json", "tmp")
            except IOError:
                pass
            FileStorage.__objects = {}

        @classmethod
        def tearDown(self):
            try:
                os.remove("file.json")
            except IOError:
                pass
            try:
                os.rename("tmp", "file.json")
            except IOError:
                pass
            storage.reload()

            correct = "** class name missing **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(".destroy()"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** class doesn't exist **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("MyModel.destroy()"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** instance id missing **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy User"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy State"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy City"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy Place"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy Review"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** instance id missing **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("User.destroy()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("State.destroy()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("City.destroy()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Amenity.destroy()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Place.destroy()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Review.destroy()"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** no instance found **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy User 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy State 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy City 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy Amenity 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy Place 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("destroy Review 1"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** no instance found **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("User.destroy(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("State.destroy(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("City.destroy(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Amenity.destroy(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Place.destroy(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Review.destroy(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["BaseModel.{}".format(testID)]
                command = "destroy BaseModel {}".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create User"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["User.{}".format(testID)]
                command = "show User {}".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create State"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["State.{}".format(testID)]
                command = "show State {}".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Place"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["Place.{}".format(testID)]
                command = "show Place {}".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create City"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["City.{}".format(testID)]
                command = "show City {}".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Amenity"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["Amenity.{}".format(testID)]
                command = "show Amenity {}".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Review"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["Review.{}".format(testID)]
                command = "show Review {}".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())

            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["BaseModel.{}".format(testID)]
                command = "BaseModel.destroy({})".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create User"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["User.{}".format(testID)]
                command = "User.destroy({})".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create State"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["State.{}".format(testID)]
                command = "State.destroy({})".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Place"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["Place.{}".format(testID)]
                command = "Place.destroy({})".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create City"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["City.{}".format(testID)]
                command = "City.destroy({})".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Amenity"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["Amenity.{}".format(testID)]
                command = "Amenity.destroy({})".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Review"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()["Review.{}".format(testID)]
                command = "Review.destory({})".format(testID)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())

    def test_update(self):
        """Unittests for testing update from the HBNB command interpreter."""

        @classmethod
        def setUp(self):
            try:
                os.rename("file.json", "tmp")
            except IOError:
                pass
            FileStorage.__objects = {}

        @classmethod
        def tearDown(self):
            try:
                os.remove("file.json")
            except IOError:
                pass
            try:
                os.rename("tmp", "file.json")
            except IOError:
                pass

            correct = "** class name missing **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(".update()"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** class doesn't exist **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update MyModel"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("MyModel.update()"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** instance id missing **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update User"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update State"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update City"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update Amenity"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update Place"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update Review"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** instance id missing **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("BaseModel.update()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("User.update()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("State.update()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("City.update()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Amenity.update()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Place.update()"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Review.update()"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** no instance found **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update BaseModel 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update User 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update State 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update City 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update Amenity 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update Place 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("update Review 1"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** no instance found **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("BaseModel.update(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("User.update(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("State.update(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("City.update(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Amenity.update(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Place.update(1)"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Review.update(1)"))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** attribute name missing **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
                testId = output.getvalue().strip()
                testCmd = "update BaseModel {}".format(testId)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create User"))
                testId = output.getvalue().strip()
                testCmd = "update User {}".format(testId)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create State"))
                testId = output.getvalue().strip()
                testCmd = "update State {}".format(testId)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create City"))
                testId = output.getvalue().strip()
                testCmd = "update City {}".format(testId)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Amenity"))
                testId = output.getvalue().strip()
                testCmd = "update Amenity {}".format(testId)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Place"))
                testId = output.getvalue().strip()
                testCmd = "update Place {}".format(testId)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** attribute name missing **"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
                testId = output.getvalue().strip()
                testCmd = "BaseModel.update({})".format(testId)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create User"))
                testId = output.getvalue().strip()
                testCmd = "User.update({})".format(testId)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create State"))
                testId = output.getvalue().strip()
                testCmd = "State.update({})".format(testId)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create City"))
                testId = output.getvalue().strip()
                testCmd = "City.update({})".format(testId)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Amenity"))
                testId = output.getvalue().strip()
                testCmd = "Amenity.update({})".format(testId)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Place"))
                testId = output.getvalue().strip()
                testCmd = "Place.update({})".format(testId)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** value missing **"
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create BaseModel")
                testId = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = "update BaseModel {} attr_name".format(testId)
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create User")
                testId = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = "update User {} attr_name".format(testId)
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create State")
                testId = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = "update State {} attr_name".format(testId)
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create City")
                testId = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = "update City {} attr_name".format(testId)
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Amenity")
                testId = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = "update Amenity {} attr_name".format(testId)
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Place")
                testId = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = "update Place {} attr_name".format(testId)
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Review")
                testId = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = "update Review {} attr_name".format(testId)
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())

            correct = "** value missing **"
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create BaseModel")
                testId = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = "BaseModel.update({}, attr_name)".format(testId)
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create User")
                testId = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = "User.update({}, attr_name)".format(testId)
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create State")
                testId = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = "State.update({}, attr_name)".format(testId)
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create City")
                testId = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = "City.update({}, attr_name)".format(testId)
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Amenity")
                testId = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = "Amenity.update({}, attr_name)".format(testId)
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Place")
                testId = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = "Place.update({}, attr_name)".format(testId)
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Review")
                testId = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = "Review.update({}, attr_name)".format(testId)
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create BaseModel")
                testId = output.getvalue().strip()
            testCmd = "update BaseModel {} attr_name \
                'attr_value'".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["BaseModel.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create User")
                testId = output.getvalue().strip()
            testCmd = "update User {} attr_name 'attr_value'".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["User.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create State")
                testId = output.getvalue().strip()
            testCmd = "update State {} attr_name 'attr_value'".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["State.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create City")
                testId = output.getvalue().strip()
            testCmd = "update City {} attr_name 'attr_value'".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["City.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Place")
                testId = output.getvalue().strip()
            testCmd = "update Place {} attr_name 'attr_value'".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["Place.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Amenity")
                testId = output.getvalue().strip()
            testCmd = "update Amenity {} attr_name 'attr_value'".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["Amenity.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Review")
                testId = output.getvalue().strip()
            testCmd = "update Review {} attr_name 'attr_value'".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["Review.{}".format(testId)].__dict__
            self.assertTrue("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create BaseModel")
                tId = output.getvalue().strip()
            testCmd = "BaseModel.update({}, attr_name, \'attr_value')".format(tId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["BaseModel.{}".format(tId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create User")
                tId = output.getvalue().strip()
            testCmd = "User.update({}, attr_name, 'attr_value')".format(tId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["User.{}".format(tId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create State")
                tId = output.getvalue().strip()
            testCmd = "State.update({}, attr_name, 'attr_value')".format(tId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["State.{}".format(tId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create City")
                tId = output.getvalue().strip()
            testCmd = "City.update({}, attr_name, 'attr_value')".format(tId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["City.{}".format(tId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Place")
                tId = output.getvalue().strip()
            testCmd = "Place.update({}, attr_name, 'attr_value')".format(tId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["Place.{}".format(tId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Amenity")
                tId = output.getvalue().strip()
            testCmd = "Amenity.update({}, attr_name, 'attr_value')".format(tId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["Amenity.{}".format(tId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Review")
                tId = output.getvalue().strip()
            testCmd = "Review.update({}, attr_name, 'attr_value')".format(tId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["Review.{}".format(tId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Place")
                testId = output.getvalue().strip()
            testCmd = "update Place {} max_guest 98".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["Place.{}".format(testId)].__dict__
            self.assertEqual(98, test_dict["max_guest"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Place")
                tId = output.getvalue().strip()
            testCmd = "Place.update({}, max_guest, 98)".format(tId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["Place.{}".format(tId)].__dict__
            self.assertEqual(98, test_dict["max_guest"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Place")
                testId = output.getvalue().strip()
            testCmd = "update Place {} latitude 7.2".format(testId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["Place.{}".format(testId)].__dict__
            self.assertEqual(7.2, test_dict["latitude"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Place")
                tId = output.getvalue().strip()
            testCmd = "Place.update({}, latitude, 7.2)".format(tId)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["Place.{}".format(tId)].__dict__
            self.assertEqual(7.2, test_dict["latitude"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create BaseModel")
                testId = output.getvalue().strip()
            testCmd = "update BaseModel {} ".format(testId)
            testCmd += "{'attr_name': 'attr_value'}"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["BaseModel.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create User")
                testId = output.getvalue().strip()
            testCmd = "update User {} ".format(testId)
            testCmd += "{'attr_name': 'attr_value'}"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["User.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create State")
                testId = output.getvalue().strip()
            testCmd = "update State {} ".format(testId)
            testCmd += "{'attr_name': 'attr_value'}"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["State.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create City")
                testId = output.getvalue().strip()
            testCmd = "update City {} ".format(testId)
            testCmd += "{'attr_name': 'attr_value'}"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["City.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Place")
                testId = output.getvalue().strip()
            testCmd = "update Place {} ".format(testId)
            testCmd += "{'attr_name': 'attr_value'}"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["Place.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Amenity")
                testId = output.getvalue().strip()
            testCmd = "update Amenity {} ".format(testId)
            testCmd += "{'attr_name': 'attr_value'}"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["Amenity.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Review")
                testId = output.getvalue().strip()
            testCmd = "update Review {} ".format(testId)
            testCmd += "{'attr_name': 'attr_value'}"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["Review.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create BaseModel")
                testId = output.getvalue().strip()
            testCmd = "BaseModel.update({}".format(testId)
            testCmd += "{'attr_name': 'attr_value'})"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["BaseModel.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create User")
                testId = output.getvalue().strip()
            testCmd = "User.update({}, ".format(testId)
            testCmd += "{'attr_name': 'attr_value'})"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["User.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create State")
                testId = output.getvalue().strip()
            testCmd = "State.update({}, ".format(testId)
            testCmd += "{'attr_name': 'attr_value'})"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["State.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create City")
                testId = output.getvalue().strip()
            testCmd = "City.update({}, ".format(testId)
            testCmd += "{'attr_name': 'attr_value'})"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["City.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Place")
                testId = output.getvalue().strip()
            testCmd = "Place.update({}, ".format(testId)
            testCmd += "{'attr_name': 'attr_value'})"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["Place.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Amenity")
                testId = output.getvalue().strip()
            testCmd = "Amenity.update({}, ".format(testId)
            testCmd += "{'attr_name': 'attr_value'})"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["Amenity.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Review")
                testId = output.getvalue().strip()
            testCmd = "Review.update({}, ".format(testId)
            testCmd += "{'attr_name': 'attr_value'})"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["Review.{}".format(testId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Place")
                testId = output.getvalue().strip()
            testCmd = "update Place {} ".format(testId)
            testCmd += "{'max_guest': 98})"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["Place.{}".format(testId)].__dict__
            self.assertEqual(98, test_dict["max_guest"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Place")
                testId = output.getvalue().strip()
            testCmd = "Place.update({}, ".format(testId)
            testCmd += "{'max_guest': 98})"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["Place.{}".format(testId)].__dict__
            self.assertEqual(98, test_dict["max_guest"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Place")
                testId = output.getvalue().strip()
            testCmd = "update Place {} ".format(testId)
            testCmd += "{'latitude': 9.8})"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["Place.{}".format(testId)].__dict__
            self.assertEqual(9.8, test_dict["latitude"])

            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create Place")
                testId = output.getvalue().strip()
            testCmd = "Place.update({}, ".format(testId)
            testCmd += "{'latitude': 9.8})"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()["Place.{}".format(testId)].__dict__
            self.assertEqual(9.8, test_dict["latitude"])

    def test_count(self):
        """Unittests for testing count method of HBNB comand interpreter."""

        @classmethod
        def setUp(self):
            try:
                os.rename("file.json", "tmp")
            except IOError:
                pass
            FileStorage._FileStorage__objects = {}

        @classmethod
        def tearDown(self):
            try:
                os.remove("file.json")
            except IOError:
                pass
            try:
                os.rename("tmp", "file.json")
            except IOError:
                pass

            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("MyModel.count()"))
                self.assertEqual("0", output.getvalue().strip())

            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
                self.assertEqual("1", output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create User"))
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("User.count()"))
                self.assertEqual("1", output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create State"))
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("State.count()"))
                self.assertEqual("1", output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Place"))
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Place.count()"))
                self.assertEqual("1", output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create City"))
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("City.count()"))
                self.assertEqual("1", output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
                self.assertEqual("1", output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Review"))
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Review.count()"))
                self.assertEqual("1", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
