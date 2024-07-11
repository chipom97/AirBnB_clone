#!/usr/bin/python3

"""Modules needed for the BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class for all models."""
    
    def __init__(self, *args, **kwargs):
        """If Kwargs (dictionary argument) is empty,
        Initialize BaseModel object."""

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""

        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """A function that prints the string representation"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""

        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['created_at'] = self.created_at.isoformat()
        return dict_copy
