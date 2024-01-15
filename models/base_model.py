#!/usr/bin/python3

"""Base model module"""

import uuid
from datetime import datetime
#from models import storage


class BaseModel:
    """BaseModel: defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Public Instance attributes"""
        if kwargs:
            # Remove '__class__' key if it's in the dictionary
            kwargs.pop('__class__', None)

            for key, value in kwargs.items():
                # Check if the attribute is 'created_at' or 'updated_at
                if key in ('created_at', 'updated_at'):
                    # and convert the string to datetime object
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            # If `kwargs` is empty, set the defaults for a new instance
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the BaseModel class."""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates public instance with current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the
        instance"""
        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['class'] = self.__class__.__name__
        return dict_copy
