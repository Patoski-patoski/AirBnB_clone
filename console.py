#!/usr/bin/env python3

"""Console module"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """A class HBNBCommand(cmd.Cmd), entry point of the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """To exit the program """
        exit(1)

    def do_EOF(self, line):
        """to exit the program gracefully"""
        return True

    def emptyline(self):
        """Goes to the next line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id"""

        if not arg:
            print("** class name missing **")
            return

        try:
            if arg == "BaseModel":
                new_instance = BaseModel()
            else:
                print("** class doesn't exist **")
                return
            new_instance.save()
            print(new_instance.id)

        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Shows the string representation of an instance based on the class
        name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key, None)
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances based or not on
        the class name."""
        args = arg.split()
        if len(args) > 0 and args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            print(
                    [str(obj) for obj in all_objs.values()
                     if not args or obj.__class__.__name__ == args[0]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                obj = storage.all()[key]
                # Assuming the attribute name is valid and the value is string.
                setattr(obj, args[2], args[3])
                obj.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
