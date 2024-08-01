#!/usr/bin/python3
"""Defines a BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Represents the BaseModel for the project."""

    def __init__(self, *args, **kwargs):
        """Will be initialised using a dictionary."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # datetime is coverted from string to object
                    value = datetime.fromisoformat(value)
                elif key == "__class__":
                    # Skip setting the special '__class__' attribute
                    continue
                    # sets (self, key, vale) for remaing attributes
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Retrurn a string description of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at to the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary of the BaseModel, these will be used to
        initialise a new instance except for __class__.
        we make a copy of the original dictionary so that we can see,
        test cases where new attributes are added"""
        rdict = self.__dict__.copy()
        # copy the dictionary and modify it and return the modified on
        # we are adding a new key __class__ while making datetime strings
        # id is okay, so we skip it
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
