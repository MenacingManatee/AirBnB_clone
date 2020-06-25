#!/usr/bin/python3
'''BaseModel Module'''

import uuid
from datetime import datetime


class BaseModel():
    '''class BaseModel defines common attributes/methods for other classes'''

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        '''updates public instance attr updated_at with current datetime'''
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        '''returns a dict containing all keys/values of __dict__ of instance'''
        self_dict = {}
        for item in self.__dict__:
            self_dict.update({item: self.__dict__.get(item)})
        self_dict.update({'__class__': self.__class__.__name__})
        return self_dict

    def __str__(self):
        '''should print: [<class name>] (<self.id>) <self.__dict__>'''
        return "[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__)
