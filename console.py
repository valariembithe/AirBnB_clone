#!/usr/bin/env python3
"""This is the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
