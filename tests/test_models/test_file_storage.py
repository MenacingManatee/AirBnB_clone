#!/usr/bin/python3
'''Tests the file storage of the module'''
import unittest
from models import *


class Test_File_Storage(unittest.TestCase):
    '''Tests the file storage of the module'''

    def setUp(self):
        '''Instantiates all the objects used in tests'''
        self.b = base_model.BaseModel()
        self.b.save()

    def test_base_model(self):
        '''Tests for basemodel being saved to a file'''
        with open('file.json', "r") as f:
            import json
            dic = json.loads(f.read())
            b_id = "BaseModel.{}".format(self.b.id)
            obj = dic[b_id]
            self.assertTrue(b_id in dic)
            self.assertTrue(obj['id'] == self.b.id)
            try:
                # This also tests to ensure to_dict() exists
                b_dict = self.b.to_dict()
            except Exception:
                return False
            self.assertTrue(obj['created_at'] == b_dict['created_at'])
            self.assertTrue(obj['updated_at'] == b_dict['updated_at'])
            self.assertTrue(obj == self.b.to_dict())
            f.close()
        self.b.__dict__.update({"first_name": "Joshua"})
        self.b.save()
        with open('file.json', "r") as f:
            import json
            dic = json.loads(f.read())
            obj = dic["BaseModel.{}".format(self.b.id)]
            self.assertTrue('first_name' in obj)
            f.close()

    def test_amenity(self):
        '''Tests for amenity being saved to a file'''
