"""Base model module"""

import uuid
from datetime import datetime, date, timedelta, time, tzinfo


class BaseModel:
    """BaseModel: defines all common attributes/methods for other classes"""

    def __init__(self):
        """Public Instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the BaseModel class."""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates public instance with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self, ):
        """updates the attribute <updated_at> with the current datetime"""
        
        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['class'] = self.__class__.__name__
        return dict_copy
