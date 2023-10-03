#!/usr/bin/env python3
"""Command interpreter module"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    # quit
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    # exit
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    # emptyline
    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    # create
    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    # show
    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = storage.all()

        if key not in all_objects:
            print("** no instance found **")
            return

        print(all_objects[key])

    # destroy
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = storage.all()

        if key not in all_objects:
            print("** no instance found **")
            return

        del all_objects[key]
        storage.save()

    # all
    def do_all(self, arg):
        """Prints all string representation of all instances"""
        class_name = arg if arg else None
        if class_name and class_name not in globals():
            print("** class doesn't exist **")
            return

        all_objects = storage.all()

        if class_name:
            instances = [str(obj) for key, obj in all_objects.items()
                         if key.startswith(class_name + ".")]
        else:
            instances = [str(obj) for obj in all_objects.values()]

        print(instances)

    # update
    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = storage.all()

        if key not in all_objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        value_str = args[3]
        # Check if the value is wrapped in double quotes
        if value_str[0] == '"' and value_str[-1] == '"':
            value = value_str[1:-1]
        else:
            value = value_str

        obj = all_objects[key]
        setattr(obj, attr_name, value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
