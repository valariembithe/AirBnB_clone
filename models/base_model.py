#!/usr/bin/env python3
import models
import uuid
from datetime import datetime
"""
This module defines all common attributes/methods for other classes
"""


class BaseModel:
    """
    A base class defining common attributes and methods for other classes.

    Public instance attributes:
    - id (string): A unique identifier assigned when an instance is created.
    - created_at (datetime): The date and time when an instance is created.
    - updated_at (datetime): The date and time when an instance is updated.

    Public instance methods:
    - __str__(self): Returns a string representation of the object.
    - save(self): Updates the public instance attribute 'updated_at'\
    with the current datetime.
    - to_dict(self): Returns a dictionary containing all keys/values\
    of __dict__ of the instance.

   Usage:
    The BaseModel class is designed to be inherited by other classes to\
    provide common attributes and methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            if "__class__" in kwargs:
                kwargs.pop("__class__")

            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representaton of the BaseModel odject.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the "updated_at" attribute with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
