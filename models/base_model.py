#!/usr/bin/python3

"""Define Basemodel Class"""

import uuid
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the AirBnB Console"""

    def __init__(self, *args, **kwargs):
        """Initialize a new Basemodel"""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        
    def __str__(self):
        """Return the string representation of a BaseModel instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """update to current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance"""
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
