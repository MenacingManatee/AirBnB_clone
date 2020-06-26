#!/usr/bin/python3
'''Entry point for command line'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''command interpreter'''
    prompt = "(hbnb) "

    def do_EOF(self, args):
        '''Quit command to exit the program'''
        exit()

    def do_quit(self, args):
        '''Quit command to exit the program'''
        exit()


if __name__ == '__main__':
    interpreter=HBNBCommand()
    interpreter.cmdloop()
