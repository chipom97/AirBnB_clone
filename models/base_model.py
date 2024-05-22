#!/usr/bin/python3
"""
Modules needed for the BaseModel class
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """

Base class for aall models.

This class provides a base for all other models,
containing common public attributes such as ID,
creation timestamp, and last update timestamp.
"""
    def __init__(self):
        """

Initialize BaseModel object.
Parameters:
- id: The ID of object
- created_at: The creation timestamp
- updated_at: The last update timestamp
"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """

updates the public instance attribute
updated_at with the current datetime
"""
        self.updated_at = datetime.now()

    def __str__(self):
        """

A function that prints [<class name>] (<self.id>) <self.__dict__>
"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """

returns a dictionary containing all keys/values
of __dict__ of the instance
"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = sel.updated_at.isoformat()
        return dict_copy
