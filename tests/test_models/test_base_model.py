#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
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

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

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
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_str(self):
        """ Testing __str__ method """
        i = self.value()
        expected_output = '[{}] ({}) {}'.format(self.name, i.id, i.__dict__)
        self.assertEqual(str(i), expected_output)

    def test_todict(self):
        """ Testing to_dict method """
        i = self.value()
        i_dict = i.to_dict()

        # Check if the returned value is a dictionary
        self.assertIsInstance(i_dict, dict)

        # Check if the dictionary contains the required keys
        self.assertIn('id', i_dict)
        self.assertIn('created_at', i_dict)
        self.assertIn('updated_at', i_dict)

        # Check if the values of the keys are of the correct types
        self.assertIsInstance(i_dict['id'], str)
        self.assertIsInstance(i_dict['created_at'], str)
        self.assertIsInstance(i_dict['updated_at'], str)

        # Check if the values of the keys are correct
        self.assertEqual(i_dict['id'], i.id)
        self.assertEqual(i_dict['created_at'], i.created_at.isoformat())
        self.assertEqual(i_dict['updated_at'], i.updated_at.isoformat())

        # Check if the dictionary contains the __class__ key
        self.assertIn('__class__', i_dict)

        # Check if the value of the __class__ key is the class name
        self.assertEqual(i_dict['__class__'], self.name)
