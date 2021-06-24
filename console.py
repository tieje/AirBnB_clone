"""
Entry point of the command interpreter
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    The entry point of the command interpreter
    """
    prompt = '(hbnb)'
    def __init__(self):
        super().__init__()
        if self.stdin == 'quit':
            quit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
