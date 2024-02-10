#!/usr/bin/env python3

import cmd
import json
import os


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""
    prompt = "(hbnb) "

    def quit(self):
        """Quit command to exit the program"""
        self.do_exit()
        return True

    do_quit = quit
    do_EOF = quit

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True
    
    def emptyline(self):
        """Do nothing when receiving an empty command"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()