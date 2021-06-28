#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd, json, shlex
from models import storage, class_names_list
from models.amenity import Amenity
from models.city import City
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    """
    The entry point of the command interpreter
    """
    prompt = '(hbnb) '
    cls_name_missing_msg = "** class name missing **"
    inst_id_missing_msg = "** instance id missing **"
    class_dne_msg = "** class doesn't exist **"
    no_instance_found_msg = "** no instance found **"
    attribute_missing_msg = "** attribute name missing **"
    value_missing_msg = "** value missing **"

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
        parsed_args = HBNBCommand.parse_arg(arg)
        if HBNBCommand.missing_args(parsed_args, 0, HBNBCommand.cls_name_missing_msg):
            return
        if not HBNBCommand.class_exists(parsed_args):
            return
        new_model = eval(parsed_args[0])()
        new_model.save()
        print(new_model.id)

    def do_show(self, arg):
        '''
        prints string rep of instace based on
        class name and id
        This code assumes that the ID will exist
        '''
        parsed_args = HBNBCommand.parse_arg(arg)
        if HBNBCommand.missing_args(parsed_args, 0, HBNBCommand.cls_name_missing_msg):
            return
        if not HBNBCommand.class_exists(parsed_args):
            return
        if HBNBCommand.missing_args(parsed_args, 1, HBNBCommand.inst_id_missing_msg):
            return
        print_this = HBNBCommand.json_class_id_exists(parsed_args)
        if print_this:
            print(print_this)

    def do_destroy(self, arg):
        '''
        Deletes an instance based on class name
        and id
        '''
        parsed_args = HBNBCommand.parse_arg(arg)
        if HBNBCommand.missing_args(parsed_args, 0, HBNBCommand.cls_name_missing_msg):
            return
        if not HBNBCommand.class_exists(parsed_args):
            return
        if HBNBCommand.missing_args(parsed_args, 1, HBNBCommand.inst_id_missing_msg):
            return
        destroy_this = HBNBCommand.json_class_id_exists(parsed_args)
        if destroy_this:
            obj = parsed_args[0] + '.' + parsed_args[1]
            del storage.all()[obj]
            storage.save()

    def do_all(self, arg):
        '''
        prints all string reps of all instances
        '''
        parsed_args = HBNBCommand.parse_arg(arg)
        if parsed_args == [''] or parsed_args == [] or parsed_args == None:
            print_list = []
            for key in storage.all():
                print_list.append(str(storage.all()[key]))
            print(print_list)
            return
        if not HBNBCommand.class_exists(parsed_args):
            return
        print_list = []
        for key in storage.all():
            if parsed_args[0] == key[:len(parsed_args[0])]:
                print_list.append(str(storage.all()[key]))
        print(print_list)

    def do_update(self, arg):
        '''
        Updates an instance based on
        class name and id by adding or
        updating attribute
        '''
        parsed_args = HBNBCommand.parse_arg(arg)
        if HBNBCommand.missing_args(parsed_args, 0, HBNBCommand.cls_name_missing_msg):
            return
        if not HBNBCommand.class_exists(parsed_args):
            return
        if HBNBCommand.missing_args(parsed_args, 1, HBNBCommand.inst_id_missing_msg):
            return
        if not HBNBCommand.json_class_id_exists(parsed_args):
            return
        if HBNBCommand.missing_args(parsed_args, 2, HBNBCommand.attribute_missing_msg):
            return
        if HBNBCommand.missing_args(parsed_args, 3, HBNBCommand.value_missing_msg):
            return
        setattr(storage.all()[parsed_args[0] + '.' + parsed_args[1]],
                parsed_args[2],
                parsed_args[3])
        storage.save()

    @staticmethod
    def parse_arg(args):
        '''
        returns a string of arguments.
        This is unfinished. Regular expressions will be needed
        to account for quotation marks.
        - extra spaces might need to be accounted for as well
        '''
        arg_str = args.strip()
        spaced_arguments = shlex.split(arg_str)
        return spaced_arguments

    @staticmethod
    def class_exists(args):
        '''
        checks if the class exists
        '''
        if args[0] in class_names_list:
            return True
        print(HBNBCommand.class_dne_msg)
        return False

    @staticmethod
    def json_class_id_exists(args):
        '''
        checks if the instance exists in json file
        '''
        try:
            instance_found = storage.all()[args[0] + '.' + args[1]]
            return instance_found
        except KeyError:
            print(HBNBCommand.no_instance_found_msg)
            return False

    @staticmethod
    def missing_args(args, expected_index, msg):
        '''
        checks if a term is missing in arguments
        '''
        if len(args) < expected_index + 1:
            print(msg)
            return True
        if not args[expected_index]:
            print(msg)
            return True
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
