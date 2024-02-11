#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_Init
    TestBaseModel_Save
    TestBaseModel_To_dict
"""
from models.base_model import BaseModel
from unittest.mock import patch
import datetime
from datetime import timedelta
import models


import unittest

class TestBaseModel__Init__(unittest.TestCase):

    def test_init_with_default_values(self):
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_init_with_custom_values(self):
        base_model = BaseModel(1, "test", [1, 2, 3])
        self.assertEqual(base_model.id, 1)
        self.assertEqual(base_model.created_at, "test")
        self.assertEqual(base_model.updated_at, [1, 2, 3])

    def test_init_with_dict_custom_values(self):
        base_model = BaseModel({"id": 1, "created_at": "test", "updated_at": [1, 2, 3]})
        self.assertEqual(base_model.id, 1)
        self.assertEqual(base_model.created_at, "test")
        self.assertEqual(base_model.updated_at, [1, 2, 3])

    def test_init_with_empty_dict(self):
        base_model = BaseModel({})
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_init_with_dict_created_updated_keys(self):
        base_model = BaseModel({"created_at": "test"})
        self.assertIsNotNone(base_model.id)
        self.assertEqual(base_model.created_at, "test")
        self.assertIsNotNone(base_model.updated_at)

        base_model = BaseModel({"updated_at": "test"})
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertEqual(base_model.updated_at, "test")

    def test_init_with_dict_invalid_keys(self):
        base_model = BaseModel({"invalid_key": "test"})
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_no_arguments(self):
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

class TestBaseModel_Save(unittest.TestCase):

    def test_save_updates_updated_at(self):
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        new_updated_at = obj.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_save_calls_storage_save(self):
        obj = BaseModel()
        with patch('models.storage.save') as mock_save:
            obj.save()
            mock_save.assert_called_once()

    def test_save_updates_existing_updated_at(self):
        obj = BaseModel()
        obj.updated_at = datetime.now() - timedelta(days=1)
        old_updated_at = obj.updated_at
        obj.save()
        new_updated_at = obj.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_save_does_not_update_created_at(self):
        obj = BaseModel()
        obj.created_at = datetime.now() - timedelta(days=1)
        old_created_at = obj.created_at
        obj.save()
        new_created_at = obj.created_at
        self.assertEqual(old_created_at, new_created_at)

    def test_save_updates_updated_at_multiple_times(self):
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        new_updated_at = obj.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        old_updated_at = new_updated_at
        obj.save()
        new_updated_at = obj.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_save_no_exception_when_storage_not_set(self):
        obj = BaseModel()
        models.storage = None
        try:
            obj.save()
        except:
            self.fail("save() raised an exception when storage was not set")


class TestBaseModel_To_dict(unittest.TestCase):

    def test_returns_dictionary_with_all_attributes(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['id'], base_model.id)
        self.assertEqual(base_model_dict['created_at'],
                         base_model.created_at.isoformat())
        self.assertEqual(base_model_dict['updated_at'],
                         base_model.updated_at.isoformat())
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')

    def test_dictionary_contains_correct_time_values(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict['created_at'],
                         base_model.created_at.isoformat())
        self.assertEqual(base_model_dict['updated_at'],
                         base_model.updated_at.isoformat())

    def test_dictionary_contains_correct_class_attribute_value(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')

    def test_base_model_has_no_attributes(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(len(base_model_dict), 4)

    def test_base_model_has_attributes_with_none_values(self):
        base_model = BaseModel()
        base_model.name = None
        base_model.age = None
        base_model_dict = base_model.to_dict()
        self.assertIsNone(base_model_dict['name'])
        self.assertIsNone(base_model_dict['age'])

    def test_base_model_has_attributes_with_complex_values(self):
        base_model = BaseModel()
        base_model.list_attr = [1, 2, 3]
        base_model.dict_attr = {'key': 'value'}
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict['list_attr'], [1, 2, 3])
        self.assertEqual(base_model_dict['dict_attr'], {'key': 'value'})
