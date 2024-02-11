#!/usr/bin/env python3
"""Defines the HBNB console."""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models import storage

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Review",
        "Amenity",
    }

    def emptyline(self):
        """Do nothing when receiving an empty command."""
        pass

    def default(self, args):
        """This function is the default method for the interpreter."""

        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
        }

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        print("")
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it
                    (to the JSON file) and prints the id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            storage.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an
                instance based on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, args):
        """Prints all string representation of
                    all instances based or not on the class name"""
        args = args.split()
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if len(args) == 0 or args[0] == key.split(".")[0]:
                    print(value)

    def do_count(self, args):
        """Counts the number of instances of a given class."""
        args = args.split()
        count = 0
        for key in storage.all():
            if key.split(".")[0] == args[0]:
                count += 1
        print(count)

    def do_update(self, args):
        """Updates an instance based on
                the class name and id by adding or updating attribute"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                setattr(storage.all()[key], args[2], args[3])
                storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
