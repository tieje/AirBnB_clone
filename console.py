#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    The entry point of the command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """quit command quits console"""
        quit()

    def do_EOF(self, arg):
        """EOF command quits the console"""
        quit()

    def emptyline(self):
        """
        Override emptyline() to return nothing
        instead of the last line
        """
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
