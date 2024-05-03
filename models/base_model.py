#!/usr/bin/python3
# Write a class BaseModel that defines all common attributes/methods for other classes:

# models/base_model.py
# Public instance attributes:
# id: string - assign with an uuid when an instance is created:
# you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
# the goal is to have unique id for each BaseModel
# created_at: datetime - assign with the current datetime when an instance is created
# updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
# __str__: should print: [<class name>] (<self.id>) <self.__dict__>
# Public instance methods:
# save(self): updates the public instance attribute updated_at with the current datetime
# to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
# by using self.__dict__, only instance attributes set will be returned
# a key __class__ must be added to this dictionary with the class name of the object
# created_at and updated_at must be converted to string object in ISO format:
# format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
# you can use isoformat() of datetime object
# This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel

import uuid
from datetime import datetime


class BaseModel():
    """BaseModel class"""

    def __init__(self):
        """BaseModel constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at attribute with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of BaseModel instance"""
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
