#!/usr/bin/python3
"""
Tests for the Base Model
"""
import unittest
import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Tests for BaseModel class
    """
    def setUp(self):
        '''setup for tests'''
        self.test_model = BaseModel()
        self.test_model.name = "Holberton"
        self.test_model.my_number = 89

    def test_attributes_are_string(self):
        '''test if id exists and is string type'''
        self.assertEqual(type(self.test_model.id), str)
        self.assertEqual(type(self.test_model.created_at), str)
        self.assertEqual(type(self.test_model.updated_at), str)
    
    def test_str_print(self):
        '''Test the result of __str__'''
        self.assertEqual(print(self.test_model),
            '[BasemModel] (' + self.test_model.id +' ) ' + str(self.test_model.to_dict()) )
    
    def test_save(self):
        '''Tests save() method'''
        old = self.test_model.updated_at
        self.test_model.save()
        new = self.test_model.updated_at
        self.assertNotEqual(old, new)
    
    def test_to_dict(self):
        '''Tests if dictionary type is returned'''
        self.assertEqual(type(self.test_model.to_dict), dict)
    
    