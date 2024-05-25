#!/usr/bin/python3

import os
import json


class FileStorage:
    """
serializes instances to a JSON file
and deserializes JSON file to instances
"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
Provide access to all objects stored with the file storage
"""
        return self.__objects

    def new(self, obj):
        """
add a new object to the internal dictionary __objects
takes an object as an arguement (class names)
sets the value of the key to the contents of the class name
"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
create a dictionary to save the serialised information
to_dict is the dictiionary format needed for a proper
serialization process
"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                serialized_objects = json.load(file)

            for key, serialized_obj in serialized_objects.items():
                class_name, obj_id = key.split('.')

                from models.base_model import BaseModel

                obj_class = BaseModel.class_map.get(class_name)
                if obj_class:
                    self.__objects[key] = obj_class(**serialized_obj)
                else:
                    print(f"Class '{class_name}' not found.")
