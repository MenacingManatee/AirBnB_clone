#!/usr/bin/python3
'''Entry point for command line'''
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import sys


class HBNBCommand(cmd.Cmd):
    '''command interpreter'''
    prompt = "(hbnb) "
    class_names = [
        'BaseModel', 'User', 'State', 'City',
        'Amenity', 'Place', 'Review']

    def precmd(self, args):
        '''Used to check for class.command methods before being sent to
        command processing'''
        if args != '':
            check = args.split(".")
            if check[0] in self.class_names:
                if len(check) > 1 and check[1] == 'all()':
                    return "all {}".format(check[0])
                elif len(check) > 1 and check[1] == 'count()':
                    return "count {}".format(check[0])
                elif len(check) > 1 and 'update(' in check[1]:
                    import re
                    if '{' in check[1]:
                        args = check[1].split(", ", 1)
                        oid = args[0].split('(')
                        d = args[1].strip(")")
                        d = d.strip()
                        d = d.replace('\'', '\"')
                        return "update_dict {} {}".format(check[0] + '.' +
                                                          "".join(oid[1:]), d)
                    delims = "(", ")", ", "
                    delimPatt = '|'.join(map(re.escape, delims))
                    args = re.split(delimPatt, args)
                    return ("update {} {} {} {}".format(check[0],
                                                        args[1].strip('\"'),
                                                        args[2].strip('\"\''),
                                                        args[3].strip('\"\'')))
        return args

    def do_update_dict(self, arg):
        '''Updates an object using a dictionary'''
        args = arg.split(' ', 1)
        oid = args[0]
        dict1 = args[1]
        if dict1 is None or dict1 == '':
            print("** Dictionary missing **")
            return
        instances = storage.all()
        if oid not in instances:
            print("** no instance found **")
            return
        import json
        from datetime import datetime
        dict1 = json.loads(dict1)
        utime = str(datetime.now())
        dict1['updated_at'] = utime
        instances[oid].update(dict1)
        storage.new(instances)
        storage.save()
        return

    def do_count(self, args):
        '''Counts the number of instances of an object'''
        objs = storage.all()
        count = 0
        for item in objs:
            if args in item:
                count += 1
        print(count)

    def do_EOF(self, args):
        '''Quit command to exit the program'''
        if not sys.stdin.isatty():
            print("")
        exit()

    def do_quit(self, args):
        '''Quit command to exit the program'''
        exit()

    def do_create(self, args):
        '''Create instance of class, saves it to JSON file, prints id'''
        if args == '':
            print('** class name missing **')
            return
        if args in self.class_names:
            '''class_dict = {'User': User(), 'State': State(),
                          'City': City(), 'Amenity': Amenity(),
                          'Place': Place(), 'Review': Review(),
                          'BaseModel': BaseModel()}'''
            if args == 'User':
                instance = User()
            elif args == 'State':
                instance = State()
            elif args == 'City':
                instance = City()
            elif args == 'Amenity':
                instance = Amenity()
            elif args == 'Place':
                instance = Place()
            elif args == 'Review':
                instance = Review()
            else:
                instance = BaseModel()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")
            return

    def do_show(self, args):
        '''Shows object based on class and id'''
        if args == '':
            print('** class name missing **')
            return
        list_args = self.parse(args)
        class_name = list_args[0]
        if class_name not in self.class_names:
            print("** class doens't exist **")
            return
        if len(list_args) < 2:
            print('** instance id missing **')
            return
        dict_instances = storage.all()
        key = list_args[0] + '.' + list_args[1]
        if key in dict_instances:
            print(dict_instances[key])
        else:
            print('** no instance found **')

    def do_destroy(self, args):
        '''Deletes an object based on class and id'''
        if args == '':
            print('** class name missing **')
            return
        list_args = self.parse(args)
        class_name = list_args[0]
        if class_name not in self.class_names:
            print("** class doens't exist **")
            return
        if len(list_args) < 2:
            print('** instance id missing **')
            return
        dict_instances = storage.all()
        key = list_args[0] + '.' + list_args[1]
        if key in dict_instances:
            dict_instances.pop(key)
        else:
            print('** no instance found **')

    def do_all(self, args):
        '''prints all saved objects'''
        if args == '':
            objs = storage.all()
            pr = []
            for item in objs:
                pr.append({item: objs[item]})
            print(pr)
            return
        if args not in self.class_names:
            print("** class doesn't exist **")
        else:
            dict_instances = storage.all()
            list_instances = []
            for keys in dict_instances:
                if args in keys:
                    list_instances.append({keys: dict_instances[keys]})
            print(list_instances)

    def do_update(self, args):
        '''updates'''
        if args == '':
            print("** class name missing **")
            return
        list_args = self.parse([args])
        class_name = list_args[0]
        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return
        if len(list_args) < 2:
            print("** instance id missing **")
            return
        if len(list_args) < 3:
            print("** attribute name missing **")
            return
        if len(list_args) < 4:
            print("** value missing **")
            return

        dict_instances = storage.all()
        uuid = list_args[0] + '.' + list_args[1]
        if uuid not in dict_instances:
            print("** no instance found **")
            return
        from datetime import datetime
        dict_instances[uuid].update({list_args[2]: list_args[3].strip('\"'),
                                     'updated_at': str(datetime.now())})
        storage.new(dict_instances)
        storage.save()

    def parse(self, string):
        '''splits str into list of words'''
        string = str(string)
        string = string.strip("[\"\']")
        list_args = string.split(' ')
        return list_args


if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()
