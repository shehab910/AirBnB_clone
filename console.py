#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models import storage

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
}


class HBNBCommand(cmd.Cmd):
    """This class is the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, line):
        """Create command to create a new instance of BaseModel"""
        if len(line) == 0:
            print("** class name missing **")
            return
        if line not in classes.keys():
            print("** class doesn't exist **")
            return
        new = globals()[line]()
        storage.save()
        print(new.id)

    def do_show(self, line):
        """Show command to print the string representation of an instance"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, line):
        """Destroy command to delete an instance"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """All command to print all instances"""
        if len(line) == 0:
            print([str(obj) for obj in storage.all().values()])
            return
        if line not in classes.keys():
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in storage.all().values()
              if obj.__class__.__name__ == line])

    def do_update(self, line):
        """Update command to update an instance"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, args[2], args[3])
        storage.save()

    def do_count(self, line):
        """Count command to count the number of instances"""
        if len(line) == 0:
            print(len(storage.all()))
            return
        if line not in classes.keys():
            print("** class doesn't exist **")
            return
        print(len([obj for obj in storage.all().values()
                  if obj.__class__.__name__ == line]))

    def precmd(self, line: str) -> str:
        """This method is called before the command is executed"""
        if "." in line and "(" in line:
            command, className, args = parse_word_cmd(line)
            line = "{} {} {}".format(command, className, " ".join(args))
        return super().precmd(line)


def parse_word_cmd(line: str) -> tuple[str, str, list[str]]:
    """This function parses a word command"""
    cmds = line.split(".")
    className = cmds[0]
    argsStartI = cmds[1].find("(")
    command = cmds[1][:argsStartI]
    args = cmds[1][argsStartI+1:-1].split(",")
    args = [arg.strip(" \"\'") for arg in args]
    return command, className, args


if __name__ == "__main__":
    HBNBCommand().cmdloop()
