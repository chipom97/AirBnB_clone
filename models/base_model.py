#!/usr/bin/python3
"""Defines a BaseModel class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel for the project."""

    def __init__(self, *args, **kwargs):
        """Will be initialised using a dictionary."""
        if kwargs:
            for key, value in kwargs.itmes():
                if key == "created_at" or key == "updated_at":
                    # datetime is coverted from string to object
                    value = datetime.fromisoformat(value)
                    # sets (self, key, vale) for remaing attributes
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Retrurn a string description of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at to the current datetime"""
        self.update_at = datetime.now()

    def to_dict(self):
        """Return a dictionary of the BaseModel"""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': self.__class__.__name__
            }
