#!/usr/bin/env python3

"""Console module"""

import cmd
from models.base_model import BaseModel


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

    def do_create (self, arg):
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
        """Prints the string representation of an instance based on the class
        name and id"""




if __name__ == "__main__":
    HBNBCommand().cmdloop()
