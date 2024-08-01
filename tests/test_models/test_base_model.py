#!/usr/bin/python3
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    @classmethod
    def setUpClass(cls):
        """Setup for tests"""
        cls.storage = FileStorage()
        cls.storage.reload()

    def test_file_path(self):
        """Test __file_path attribute"""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        """Test __objects attribute"""
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        """Test all() method"""
        self.storage.all().clear()  # Clear storage before testing
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test new() method"""
        my_model = BaseModel()
        self.storage.new(my_model)
        key = f"{my_model.__class__.__name__}.{my_model.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test save() method"""
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()

        # Check if file.json exists and is not empty
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as f:
            data = f.read()
        self.assertGreater(len(data), 0)

    def test_reload(self):
        """Test reload() method"""
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        self.storage.reload()

        key = f"{my_model.__class__.__name__}.{my_model.id}"
        self.assertIn(key, self.storage.all())

class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Setup for tests"""
        cls.storage = FileStorage()
        cls.storage.reload()

    def test_init(self):
        """Test __init__ method"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_save(self):
        """Test save() method"""
        obj = BaseModel()
        self.storage.new(obj)
        obj.save()
        self.assertGreater(obj.updated_at, obj.created_at)

if __name__ == "__main__":
    unittest.main()
