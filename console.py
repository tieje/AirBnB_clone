#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel


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

    def do_create(self, arg):
        '''
        Creates a new instance of BaseModel,
        saves it, and print the id
        '''
        if not arg:
            print('** class name missing **')
            return
        if arg != 'BaseModel':
            print("** class doesn't exist **")
            return
        new_model = BaseModel()
        new_model.save()
        print(new_model.id)

    def do_show(self, arg):
        '''
        prints string rep of instace based on
        class name and id
        This code assumes that the ID will exist
        '''
        args = HBNBCommand.parse_arg(arg)
        if not args[0]:
            print("** class name missing **")
            return
        if not args[1]:
            print("** instance id missing **")
        print(storage.all()[args[0] + '.' + args[1]])

    @staticmethod
    def parse_arg(arguments):
        spaced_arguments = arguments.strip().split(' ')
        return spaced_arguments


if __name__ == '__main__':
    HBNBCommand().cmdloop()
