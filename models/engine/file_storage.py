#!/usr/bin/python3
'''defines file storage class'''
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

#for case validation
new_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "City": City,
    "State": State,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class FileStorage:
    '''serializes & deserializes obj instances to JSON files'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file'''
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as the_file:
            json.dump(obj_dict, the_file, indent=2)

    def reload(self):
        '''deserializes the JSON file to __objects'''
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                job = json.load(f)
            for k in job:
                self.__objects[k] = new_dict[job[k]['__class__']](**job[k])
        except FileNotFoundError:
            pass
