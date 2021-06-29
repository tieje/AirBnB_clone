#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd
import json
import shlex
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
    cls_miss_msg = "** class name missing **"
    id_miss_msg = "** instance id missing **"
    cls_dne_msg = "** class doesn't exist **"
    no_inst_msg = "** no instance found **"
    attr_miss_msg = "** attribute name missing **"
    val_miss_msg = "** value missing **"

    def do_Amenity(self, arg):
        '''catches Amenity.<command>'''
        self.one_for_all('Amenity', arg)

    def do_BaseModel(self, arg):
        '''catches BaseModel.<command>'''
        self.one_for_all('BaseModel', arg)

    def do_City(self, arg):
        '''catches City.<command>'''
        self.one_for_all('City', arg)

    def do_Place(self, arg):
        '''catches Place.<command>'''
        self.one_for_all('Place', arg)

    def do_Review(self, arg):
        '''catches Review.<command>'''
        self.one_for_all('Review', arg)

    def do_State(self, arg):
        '''catches State.<command>'''
        self.one_for_all('State', arg)

    def do_User(self, arg):
        '''catches User.<command>'''
        self.one_for_all('User', arg)

    def one_for_all(self, cls, arg):
        '''<class>.<command> invokes this function'''
        prop_list = [
            '.all()',
            '.count()',
            '.show(',
            '.destroy(',
            '.update('
        ]
        arg_copy = arg
        for i in prop_list:
            length = len(i)
            if arg == i or i == arg[:length]:
                func = getattr(self, 'do_' + i.strip('().'))
                # cleaning input
                no_prefix = arg_copy[length:]
                split_list = no_prefix.split(',')
                def stripSpace(x): return x.strip()
                remove_Space = list(map(stripSpace, split_list))
                join_arg = ' '.join(remove_Space)
                final_arg = cls + ' ' + join_arg.strip('()')
                return func(final_arg)

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
        parsed_args = hb.parse_arg(arg)
        if hb.missing_args(parsed_args, 0, hb.cls_miss_msg):
            return
        if not hb.class_exists(parsed_args):
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
        parsed_args = hb.parse_arg(arg)
        if hb.missing_args(parsed_args, 0, hb.cls_miss_msg):
            return
        if not hb.class_exists(parsed_args):
            return
        if hb.missing_args(parsed_args, 1, hb.id_miss_msg):
            return
        print_this = hb.json_class_id_exists(parsed_args)
        if print_this:
            print(print_this)

    def do_destroy(self, arg):
        '''
        Deletes an instance based on class name
        and id
        '''
        parsed_args = hb.parse_arg(arg)
        if hb.missing_args(parsed_args, 0, hb.cls_miss_msg):
            return
        if not hb.class_exists(parsed_args):
            return
        if hb.missing_args(parsed_args, 1, hb.id_miss_msg):
            return
        destroy_this = hb.json_class_id_exists(parsed_args)
        if destroy_this:
            obj = parsed_args[0] + '.' + parsed_args[1]
            del storage.all()[obj]
            storage.save()

    def do_all(self, arg):
        '''
        prints all string reps of all instances
        '''
        pa = hb.parse_arg(arg)
        if pa == [''] or pa == [] or pa is None:
            print_list = []
            for key in storage.all():
                print_list.append(str(storage.all()[key]))
            print(print_list)
            return
        if not hb.class_exists(pa):
            return
        print_list = []
        for key in storage.all():
            if pa[0] == key[:len(pa[0])]:
                print_list.append(str(storage.all()[key]))
        print(print_list)

    def do_count(self, arg):
        '''prints number of class instances'''
        pa = hb.parse_arg(arg)
        if not hb.class_exists(pa):
            return
        counter = 0
        for key in storage.all():
            if pa[0] == key[:len(pa[0])]:
                counter += 1
        print(counter)

    def do_update(self, arg):
        '''
        Updates an instance based on
        class name and id by adding or
        updating attribute
        '''
        parsed_args = hb.parse_arg(arg)
        if hb.missing_args(parsed_args, 0, hb.cls_miss_msg):
            return
        if not hb.class_exists(parsed_args):
            return
        if hb.missing_args(parsed_args, 1, hb.id_miss_msg):
            return
        if not hb.json_class_id_exists(parsed_args):
            return
        if hb.missing_args(parsed_args, 2, hb.attr_miss_msg):
            return
        if hb.missing_args(parsed_args, 3, hb.val_miss_msg):
            return
        setattr(storage.all()[
                parsed_args[0] + '.' + parsed_args[1]],
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
        print(hb.cls_dne_msg)
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
            print(hb.no_inst_msg)
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
    hb = HBNBCommand
    HBNBCommand().cmdloop()
