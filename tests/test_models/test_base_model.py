#!/usr/bin/python3

"""test_base_model module"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TestBaseModel class for unittest case"""

    def setUp(self):
        """setup for initialization"""
        self.base_model = BaseModel()

    def test_instance_attribute(self):
        """test for public instances attributes"""
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
