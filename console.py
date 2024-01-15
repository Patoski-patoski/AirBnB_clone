#!/usr/bin/env python3

"""Console module"""

import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
