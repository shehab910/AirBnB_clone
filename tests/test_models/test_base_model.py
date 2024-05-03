import unittest
from models.base_model import BaseModel
from datetime import datetime
import json
import os
import time


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

    def test_to_dict(self):
        """ """
        b = BaseModel()
        self.assertIsInstance(b.to_dict(), dict)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertIsInstance(new.created_at, datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        # self.assertEqual(type(new.updated_at), datetime.datetime)
        self.assertIsInstance(new.created_at, datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        time.sleep(0.2)
        new.save()
        self.assertFalse(new.created_at == new.updated_at)
