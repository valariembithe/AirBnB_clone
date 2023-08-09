#!/usr/bin/env python3
"""This is the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    classes = {
        'BaseModel': BaseModel,
        'User': User
    }

    def do_quit(self, arg):
        """
        Exit the command interpreter.
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        End of file (Exit)
        Usage: Ctrl + D or EOF
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on an empty line
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Print the string representation of an instance based on
        class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on class name and id.
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print all string representations of instances.
        Usage: all or all <class name>
        """
        args = arg.split()
        instances = []
        if not args:
            for key in storage.all():
                instances.append(str(storage.all()[key]))
        elif args[0] in HBNBCommand.classes:
            for key in storage.all():
                class_name = key.split('.')[0]
                if class_name == args[0]:
                    instances.append(str(storage.all()[key]))
        else:
            print("** class doesn't exist **")
            return
        print(instances)

    def do_update(self, arg):
        """
        Update an instance based on class name and id
        with a new attribute value.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance = storage.all()[key]
        setattr(instance, args[2], args[3].strip('"'))
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
