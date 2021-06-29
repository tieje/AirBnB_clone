#!/usr/bin/python3
'''package initializer'''
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class_names_list = [
    Amenity.__name__,
    BaseModel.__name__,
    City.__name__,
    Place.__name__,
    Review.__name__,
    State.__name__,
    User.__name__,
]
storage = FileStorage()
storage.reload()
