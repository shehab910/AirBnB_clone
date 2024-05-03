#!/usr/bin/python3
"""BaseModel module"""
import uuid
from datetime import datetime


class BaseModel():
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """BaseModel constructor"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            return
        for k, v in kwargs.items():
            if k == "created_at" or k == "updated_at":
                v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
            if k != "__class__":
                setattr(self, k, v)

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
