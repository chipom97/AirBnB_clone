#!/usr/bin/python3
"""Define the file storage class"""
import json
from models.base_model import BaseModel
# to ensure that BaseModel is available for the reload method.

class FileStorage:
    """Represent a storage engine."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path),
        after they've been converted to a dictionary"""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            # call the to.dict method to convert the object to a dictionary
            obj_dict[key] = obj.to_dict()

        # write the serialized objects to the JSON file
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects if it exists"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
            # where value is the dictionary version of obj
            # we even stated class name in our code,
            # its in reference to that
            for key, value in obj_dict.items():
                class_name = value['__class__']
                if class_name == "BaseModel":
                    # the dictionary is going to be unpacked and
                    # initialised to a Basemodel with its own attributes
                    FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            # JSON file is invalid or corrupted
            print("Error: JSON file is invalid or corrupted.")
            pass
