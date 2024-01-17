#!/usr/bin/python3

import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User

my_objects = {
        "BaseModel": BaseModel,
        "User": User
}


class FileStorage:
    """Class that serializes instances to a JSON file and deserializes JSON
    file to instances."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w') as f:
            j_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(j_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                attr_dict = json.load(file)
                for obj_id, value in attr_dict.items():
                    obj = obj_id.split('.')[0]
                    FileStorage.__objects[obj_id] = my_objects[obj](**value)
