'''Test file storage file'''
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    '''test file_storage.py file'''

    def setUp(self):
        '''Initializing'''
        self.storage = FileStorage()

    def TearDown(self):
        '''Removing'''
        del self.storage

    def test_all(self):
        '''test all method'''
        self.assertEqual(type(self.storage.all()), dict)

    def test_reload(self):
        '''test reload method'''
        self.storage.reload()
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        '''test new method'''
        self.storage.reload()
        new_model = BaseModel()
        self.assertEqual(type(new_model.id), str)

    def test_save(self):
        '''test save method'''
        self.storage.reload()
        new_model = BaseModel()
        new_model.save()
        new_model_dict = new_model.to_dict()
        data = self.storage.all()['BaseModel.' + new_model_dict['id']]
        self.assertEqual(new_model_dict['id'], data.id)
