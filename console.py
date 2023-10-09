#!/usr/bin/env python3
"""Command interpreter module"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    # ... (other methods)

    def do_create(self, arg):
        """Creates a new instance of a specified class,
        saves it, and prints the id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in {"BaseModel",
                              "User",
                              "State",
                              "City",
                              "Amenity",
                              "Place",
                              "Review"}:
            print("** class doesn't exist **")
            return

        new_instance = eval(f"{class_name}()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in {"BaseModel",
                              "User",
                              "State",
                              "City",
                              "Amenity",
                              "Place",
                              "Review"}:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in {"BaseModel",
                              "User",
                              "State",
                              "City",
                              "Amenity",
                              "Place",
                              "Review"}:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if args and args[0] not in {"BaseModel",
                                    "User",
                                    "State",
                                    "City",
                                    "Amenity",
                                    "Place",
                                    "Review"}:
            print("** class doesn't exist **")
            return

        if not args:
            print([str(value) for value in storage.all().values()])
        else:
            class_name = args[0]
            print([str(value) for key, value in storage.all().items()
                   if key.startswith(class_name + ".")])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in {"BaseModel",
                              "User",
                              "State",
                              "City",
                              "Amenity",
                              "Place",
                              "Review"}:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]
        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
