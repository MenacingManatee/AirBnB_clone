#!/usr/bin/python3
'''Contains unit tests for the AirBnB console'''
import unittest
from models import *
import sys
from io import StringIO
from unittest.mock import patch
HBNBCommand = __import__('console').HBNBCommand


class test_console(unittest.TestCase):
    '''Tests for the console'''
    def test_compile(self):
        '''
        Sends no commands, just tests to make sure it compiles without error
        '''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue().strip(), "")

    def test_help(self):
        '''Tests the help command'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            out = f.getvalue().strip()
            self.assertTrue('undocumented' not in out)
            self.assertTrue('EOF' in out)
            self.assertTrue('quit' in out)
            self.assertTrue('create' in out)
            self.assertTrue('show' in out)
            self.assertTrue('destroy' in out)
            self.assertTrue('all' in out)
            self.assertTrue('update' in out)

    def test_create(self):
        '''Tests the creation of an object'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            u_id = f.getvalue().strip()
            self.assertTrue(u_id is not "")
            with open('file.json') as g:
                import json
                dic = json.loads(g.read())
                self.assertTrue("User.{}".format(u_id) in dic)
                f.close()

    def test_destroy(self):
        '''Tests the destroy console command'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            u_id = f.getvalue().strip()
            HBNBCommand().onecmd("destroy User {}".format(u_id))
            with open('file.json') as g:
                import json
                dic = json.loads(g.read())
                self.assertTrue("User.{}".format(u_id) not in dic)
                f.close()
