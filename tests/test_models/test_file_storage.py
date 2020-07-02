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
        self.a = amenity.Amenity()
        self.a.save()
        self.c = city.City()
        self.c.save()
        self.p = place.Place()
        self.p.save()
        self.r = review.Review()
        self.r.save()
        self.u = user.User()
        self.u.save()
        self.s = state.State()
        self.s.save()

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
        with open('file.json', "r") as f:
            import json
            dic = json.loads(f.read())
            a_id = "Amenity.{}".format(self.a.id)
            obj = dic[a_id]
            self.assertTrue(a_id in dic)
            self.assertTrue(obj['id'] == self.a.id)
            try:
                # This also tests to ensure to_dict() exists
                a_dict = self.a.to_dict()
            except Exception:
                return False
            self.assertTrue(obj['created_at'] == a_dict['created_at'])
            self.assertTrue(obj['updated_at'] == a_dict['updated_at'])
            self.assertTrue(obj == self.a.to_dict())
            self.assertTrue(self.a.name == '')
            f.close()
        self.a.name = "public pool"
        self.a.save()
        with open('file.json', "r") as f:
            import json
            dic = json.loads(f.read())
            obj = dic["Amenity.{}".format(self.a.id)]
            self.assertTrue(obj['name'] == "public pool")
            f.close()

    def test_city(self):
        '''Tests for city being saved to a file'''
        with open('file.json', "r") as f:
            import json
            dic = json.loads(f.read())
            c_id = "City.{}".format(self.c.id)
            obj = dic[c_id]
            self.assertTrue(c_id in dic)
            self.assertTrue(obj['id'] == self.c.id)
            try:
                # This also tests to ensure to_dict() exists and works
                c_dict = self.c.to_dict()
            except Exception:
                return False
            self.assertTrue(obj['created_at'] == c_dict['created_at'])
            self.assertTrue(obj['updated_at'] == c_dict['updated_at'])
            self.assertTrue(obj == self.c.to_dict())
            self.assertTrue(self.c.state_id == '')
            self.assertTrue(self.c.name == '')
            f.close()
        self.c.state_id = self.s.id
        self.c.name = "Tulsa"
        self.c.save()
        with open('file.json', "r") as f:
            import json
            dic = json.loads(f.read())
            obj = dic["City.{}".format(self.c.id)]
            self.assertTrue(obj['name'] == "Tulsa")
            self.assertTrue(obj['state_id'] == self.s.id)
            f.close()

    def test_place(self):
        '''Tests for place being saved to a file'''
        with open('file.json', "r") as f:
            import json
            dic = json.loads(f.read())
            p_id = "Place.{}".format(self.p.id)
            obj = dic[p_id]
            self.assertTrue(p_id in dic)
            self.assertTrue(obj['id'] == self.p.id)
            try:
                # This also tests to ensure to_dict() exists
                p_dict = self.p.to_dict()
            except Exception:
                return False
            self.assertTrue(obj['created_at'] == p_dict['created_at'])
            self.assertTrue(obj['updated_at'] == p_dict['updated_at'])
            self.assertTrue(obj == self.p.to_dict())
            f.close()
        self.assertTrue(hasattr(self.p, 'city_id'))
        setattr(self.p, 'city_id', self.c.id)
        self.assertTrue(hasattr(self.p, 'user_id'))
        setattr(self.p, 'user_id', self.u.id)
        self.assertTrue(hasattr(self.p, 'name'))
        setattr(self.p, 'name', "Home")
        self.assertTrue(hasattr(self.p, 'description'))
        setattr(self.p, 'description', 'generic description')
        self.assertTrue(hasattr(self.p, 'number_rooms'))
        setattr(self.p, 'number_rooms', 9)
        self.assertTrue(hasattr(self.p, 'number_bathrooms'))
        self.assertTrue(hasattr(self.p, 'max_guest'))
        self.assertTrue(hasattr(self.p, 'price_by_night'))
        self.assertTrue(hasattr(self.p, 'latitude'))
        self.assertTrue(hasattr(self.p, 'longitude'))
        self.assertTrue(hasattr(self.p, 'amenity_ids'))
        self.p.save()
        with open('file.json', "r") as f:
            import json
            dic = json.loads(f.read())
            obj = dic["Place.{}".format(self.p.id)]
            self.assertTrue(obj['city_id'] == self.c.id)
            self.assertTrue(obj['user_id'] == self.u.id)
            self.assertTrue(obj['name'] == "Home")
            self.assertTrue(obj['description'] == 'generic description')
            self.assertTrue(obj['number_rooms'] == 9)
            f.close()
