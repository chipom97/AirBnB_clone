#!/usr/bin/python3
"""
a convenient and organized way to initialize a package and its modules
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload(class_map)
