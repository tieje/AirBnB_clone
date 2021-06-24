#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    The entry point of the command interpreter
    """
    prompt = '(hbnb)'

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super().__init__()
        if self.stdin == 'quit' or self.stdin == 'EOF':
            quit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
