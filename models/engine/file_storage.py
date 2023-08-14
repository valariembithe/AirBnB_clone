#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

"""
    this module serializes instances to a JSON file and deserializes
    JSON file to instances
"""


class FileStorage:
    """
    Private class attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Public method that returns a dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
         sets in __objects the obj with key <obj class name>.id
         """
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file __file_path
        """
        odict = FileStorage.__objects
        obj_dict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
         deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
