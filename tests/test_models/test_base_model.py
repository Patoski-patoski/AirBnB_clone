#!/usr/bin/python3

"""test_base_model module"""


import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """TestBaseModel class for unittest case"""

    def test_create_instance_from_kwargs(self):
        """Test instance creation from dictionary."""
        # Create a dictionary representation of the BaseModel including
        # string representations of datetime objects
        # for created_at and updated_at

        current_time = datetime.now()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        kwarg_dict = {
                'id': 12345,
                'created_at': current_time.strftime(time_format),
                'updated_at': current_time.strftime(time_format)
        }

        # Create an instance of BaseModel using the dictionary
        instance = BaseModel(**kwarg_dict)

        # Asserts created_at and updated_at are datetime instances, not string
        self.assertEqual(instance.id, kwarg_dict['id'])
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

        # Asserts created_at and updated_at are correctly parsed from strings
        self.assertEqual(instance.created_at, current_time)
        self.assertEqual(instance.updated_at, current_time)

    def setUp(self):
        """setup for initialization"""
        self.base_model = BaseModel()

    def test_instance_attribute_without_kwargs(self):
        """Test instance creation without a dictionary (kwargs empty)."""
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        """test for public instance with current datetime"""
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertGreater(self.base_model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """test updates public instance attribute <updated_at> with the
        current datetime
        """
        result = self.base_model.to_dict()
        self.assertIsInstance(result, dict)
        self.assertEqual(result['class'], 'BaseModel')
        self.assertIsInstance(result['created_at'], str)
        self.assertIsInstance(result['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
