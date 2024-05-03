import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
	def test_init(self):
		""" """
		b = BaseModel()
		self.assertIsInstance(b, BaseModel)
		self.assertIsInstance(b.id, str)
		self.assertIsInstance(b.created_at, datetime)
		self.assertIsInstance(b.updated_at, datetime)

	def test_str(self):
		""" """
		b = BaseModel()
		self.assertIsInstance(b.__str__(), str)

	def test_save(self):
		""" """
		b = BaseModel()
		b.save()
		self.assertIsInstance(b.updated_at, datetime)
		self.assertNotEqual(b.created_at, b.updated_at)

	def test_to_dict(self):
		""" """
		b = BaseModel()
		self.assertIsInstance(b.to_dict(), dict)
