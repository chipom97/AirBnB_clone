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

    def test_init_with_kwargs(self):
        model_dict = {
            'id': '123e4567-e89b-12d3-a456-426614174000',
            'created_at': '2024-07-11T14:58:00.123456',
            'updated_at': '2024-07-11T14:58:00.123456',
            'name': 'MyModel'
        }
        model_instance = BaseModel(**model_dict)
        self.assertEqual(model_instance.id, '123e4567-e89b-12d3-a456-426614174000')
        self.assertEqual(model_instance.created_at, datetime.fromisoformat('2024-07-11T14:58:00.123456'))
        self.assertEqual(model_instance.updated_at, datetime.fromisoformat('2024-07-11T14:58:00.123456'))
        self.assertEqual(model_instance.name, 'MyModel')


if __name__ == '__main__':
    unittest.main()
