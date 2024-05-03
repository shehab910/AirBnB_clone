#!/usr/bin/python3
import json
from models.base_model import BaseModel
from typing import Dict
"""FileStorage module"""


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects: Dict[str, BaseModel] = {}

    def all(self):
        """Return dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Add object to __objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file"""
        d = {}
        for k, v in FileStorage.__objects.items():
            d[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(d, f)

    def reload(self):
        """Deserialize JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                d = json.load(f)
            for k, v in d.items():
                cls_name = v["__class__"]
                # Get class reference
                cls = globals()[cls_name]
                # Create object from class instructor
                obj = cls(**v)
                FileStorage.__objects[k] = obj
        except FileNotFoundError:
            pass
