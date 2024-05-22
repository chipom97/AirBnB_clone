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

    def __str__(self):
        """
        
        A function that prints [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
