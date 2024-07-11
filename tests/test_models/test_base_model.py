import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):


    def test_id(self):
        model = BaseModel()
        self.assertEqual(type(model.id), str)
        self.assertEqual(len(model.id), 36)

    def test_created_at(self):
        model = BaseModel()
        self.assertEqual(type(model.created_at), datetime)

    def test_updated_at(self):
        model = BaseModel()
        self.assertEqual(type(model.updated_at), datetime)
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_str(self):
        model = BaseModel()
        expected = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
