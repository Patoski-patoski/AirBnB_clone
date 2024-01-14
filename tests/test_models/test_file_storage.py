"""File_storage module"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """unittest for FileStorage Class"""

    def setUp(self):
        """Create a FileStorage instance and a BaseModel instance for
        testing."""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.file_path = self.storage._FileStorage__file_path

    def tearDown(self):
        """Remove the file after the test."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test that all returns the __objects dictionary."""
        self.assertEqual(
                self.storage.all(), self.storage._FileStorage__objects)

    def test_new(self):
        """Test that new adds the object to __objects with the correct key."""
        self.storage.new(self.model)
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test that save correctly serializes objects to the JSON file."""
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as f:
            lines = f.read()
            self.assertIn('BaseModel', lines)
            self.assertIn(self.model.id, lines)

    def test_reload(self):
        """Test that reload correctly deserializes objects from JSON file."""
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
