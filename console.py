#!/usr/bin/python3
'''Entry point for command line'''
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    '''command interpreter'''
    prompt = "(hbnb) "

    def do_EOF(self, args):
        '''Quit command to exit the program'''
        exit()

    def do_quit(self, args):
        '''Quit command to exit the program'''
        exit()

    def do_create(self, args):
        '''Create instance of BaseModel, saves it to JSON file, prints id'''
        if args == '':
            print('** class name missing **')
            return
        if args == 'BaseModel':
            instance = BaseModel()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")
            return

    def do_show(self, args):
        '''Shows'''
        if args == '':
            print('** class name missing **')
            return
        list_args = self.parse(args)
        if list_args[0] != 'BaseModel':
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

    def do_delete(self, args):
        '''Deletes'''
        if args == '':
            print('** class name missing **')
            return
        list_args = self.parse(args)
        if list_args[0] != 'BaseModel':
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
        '''prints all'''
        if args == '':
            print(storage.all())
            return
        if args != 'BaseModel':
            print("** class doesn't exist **")
        else:
            dict_instances = storage.all()
            list_instances = []
#            for keys in dict_instances:

    def parse(self, string):
        '''splits str into list of words'''
        list_args = string.split(' ')
        return list_args


if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()
