#!/usr/bin/python3
'''the model from which all else floweth'''
import json
import uuid
from datetime import datetime as the_time


class BaseModel():
    '''Base model defines all common attributes and methods'''

    def __init__(self, *args, **kwargs):
        ''' instantiates the attributes'''
        if len(kwargs) != 0:
            '''use kwargs to create instance'''
            for key, value in kwargs.items():
                if key == '__class__':
                    setattr(self, key, type(self))
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            the_time.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = the_time.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        '''string rep of basemodel instance'''
        return ("[{}] ({}) {}".format(type(self).__name__, self.id,
                                      self.__dict__))

    def to_dictionary(self):
        '''give dictionary representation of instance attributes'''
        new_dict = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        new_dict['__class__'] = type(self).__name__
        return new_dict
