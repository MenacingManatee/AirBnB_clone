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
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        dicti = obj.to_dict()
        self.__objects.update({"[{}] ({})".format(obj.__class__.__name__,
                                                  obj.id): dicti})

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(self.__objects))
            f.close()

    def reload(self):
        '''deserializes the JSON file to __objects'''
        try:
            with open(self.__file_path, "r") as f:
                lines = f.readlines()
                lines = json.loads(lines[0])
                for line in lines:
                    dict1 = lines.get(line)
                    if '__class__' in dict1:
                        dict1.pop('__class__')
                self.__objects.update(lines)
                f.close()
        except FileNotFoundError:
            pass
