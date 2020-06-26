#!/usr/bin/python3
'''initializes repo as a module, includes file storage'''
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
