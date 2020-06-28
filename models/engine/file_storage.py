#!/usr/bin/python3
'''serializes instances to a JSON file and deserializes JSON file to instances
'''
import json


class FileStorage():
    '''
Private class attributes:
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by <class name>.id
Public instance methods:
    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key <obj class name>.id
    save(self): serializes __objects to the JSON file (path: __file_path)
    reload(self): deserializes the JSON file to __objects
'''
    __file_path = 'file.json'
    __objects = {}

    def __init__(self, __file_path=None):
        '''Initializes file path and objects provate attribute'''
        if __file_path is not None:
            self.__file_path = __file_path

    def all(self):
        '''Returns a dictionary of all objects'''
        ret = {}
        for s, d in self.__objects.items():
            if type(d) is not dict:
                d = d.to_dict()
            c = d.copy()
            if '__class__' in d:
                c.pop('__class__')
            ret.update({s: c})
        return ret

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        if type(obj) == dict:
            self.__objects.update(obj)
        else:
            form = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects.update({form: obj})

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        with open(self.__file_path, "w") as f:
            item = {}
            for s, d in self.__objects.items():
                if type(d) is not dict:
                    item.update({s: d.to_dict()})
                else:
                    item.update({s: d})
            string = json.dumps(item)
            f.write(string)
            f.close()

    def reload(self):
        '''deserializes the JSON file to __objects'''
        try:
            with open(self.__file_path, "r") as f:
                lines = f.read()
                lines = json.loads(lines)
                for string, dic in lines.items():
                    if '__class__' in dic:
                        dic.pop('__class__')
                    self.__objects.update({string: dic})
                f.close()
        except FileNotFoundError:
            pass
