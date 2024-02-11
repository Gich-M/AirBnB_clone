from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity

import json
import unittest


class TestAll(unittest.TestCase):

    def test_returns_dictionary_of_instantiated_objects(self):
        storage = FileStorage()
        obj_dict = storage.all()
        self.assertEqual(dict, type(obj_dict))

    def test_returns_empty_dictionary_when_no_objects_added(self):
        storage = FileStorage()
        obj_dict = storage.all()
        self.assertEqual({}, obj_dict)

    def test_returns_empty_dict_when_no_objects_added_and_file_reloaded(self):
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        self.assertEqual({}, obj_dict)

    def test_returns_empty_dictionary_when_file_is_empty(self):
        with open("file.json", "w") as f:
            f.write("")
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        self.assertEqual({}, obj_dict)

    def test_returns_empty_dictionary_when_file_not_valid_JSON(self):
        with open("file.json", "w") as f:
            f.write("not valid JSON")
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        self.assertEqual({}, obj_dict)

    def test_returns_empty_dictionary_when_file_does_not_exist(self):
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        self.assertEqual({}, obj_dict)


class TestNew(unittest.TestCase):

    def test_adds_new_object_to_objects_with_key_obj_class_name_id(self):
        storage = FileStorage()
        obj = BaseModel()
        obj.id = "123"
        storage.new(obj)
        self.assertIn("BaseModel.123", storage.all())

    def test_adds_object_to_objects_dictionary(self):
        storage = FileStorage()
        obj = BaseModel()
        obj.id = "123"
        storage.new(obj)
        self.assertEqual(storage.all()["BaseModel.123"], obj)

    def test_can_add_multiple_objects_to_objects(self):
        storage = FileStorage()
        obj1 = BaseModel()
        obj1.id = "123"
        obj2 = User()
        obj2.id = "456"
        storage.new(obj1)
        storage.new(obj2)
        self.assertIn("BaseModel.123", storage.all())
        self.assertIn("User.456", storage.all())

    def test_adds_object_with_id_none_to_objects(self):
        storage = FileStorage()
        obj = BaseModel()
        obj.id = None
        storage.new(obj)
        self.assertIn("BaseModel.None", storage.all())

    def test_adds_object_with_no_id_attr_to_objects(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        self.assertIn("BaseModel.None", storage.all())

    def test_adds_object_with_id_attr_of_wrong_type_to_objects(self):
        storage = FileStorage()
        obj = BaseModel()
        obj.id = 123
        storage.new(obj)
        self.assertIn("BaseModel.123", storage.all())


class TestSave(unittest.TestCase):

    def test_save_objects_to_file(self):
        storage = FileStorage()
        user = User()
        user.save()
        with open(storage._FileStorage__file_path) as f:
            data = json.load(f)
            self.assertEqual(data, {"User.{}".format(user.id): user.to_dict()})

    def test_serialize_objects_to_file(self):
        storage = FileStorage()
        user = User()
        storage.new(user)
        storage.save()
        with open(storage._FileStorage__file_path) as f:
            data = json.load(f)
            self.assertEqual(data, {"User.{}".format(user.id): user.to_dict()})

    def test_successfully_saves_objects(self):
        storage = FileStorage()
        user = User()
        storage.new(user)
        storage.save()
        with open(storage._FileStorage__file_path) as f:
            data = json.load(f)
            self.assertEqual(data, {"User.{}".format(user.id): user.to_dict()})

    def test_saves_dictionary_with_one_object(self):
        storage = FileStorage()
        user = User()
        storage.new(user)
        storage.save()
        with open(storage._FileStorage__file_path) as f:
            data = json.load(f)
            self.assertEqual(data, {"User.{}".format(user.id): user.to_dict()})

    def test_saves_dictionary_with_multiple_objects(self):
        storage = FileStorage()
        user1 = User()
        user2 = User()
        storage.new(user1)
        storage.new(user2)
        storage.save()
        with open(storage._FileStorage__file_path) as f:
            data = json.load(f)
            self.assertEqual(data, {"User.{}".format(user1.id): user1.to_dict()
                                    , "User.{}".format(user2.id): user2.to_dict()})

    def test_saves_dictionary_with_different_classes(self):
        storage = FileStorage()
        user = User()
        state = State()
        city = City()
        place = Place()
        review = Review()
        amenity = Amenity()
        storage.new(user)
        storage.new(state)
        storage.new(city)
        storage.new(place)
        storage.new(review)
        storage.new(amenity)
        storage.save()
        with open(storage._FileStorage__file_path) as f:
            data = json.load(f)
            self.assertEqual(data, {"User.{}".format(user.id): user.to_dict(),
                                    "State.{}".format(state.id): state.to_dict(),
                                    "City.{}".format(city.id): city.to_dict(),
                                    "Place.{}".format(place.id): place.to_dict(),
                                    "Review.{}".format(review.id): review.to_dict(),
                                    "Amenity.{}".format(amenity.id): amenity.to_dict()})


class TestReload(unittest.TestCase):

    def test_loads_valid_JSON_file(self):

        storage = FileStorage()
        storage.save()  
        storage.reload()
        self.assertEqual(len(storage.all()), 0)

    def test_creates_instances_from_JSON_data(self):

        storage = FileStorage()
        user = User()
        user.name = "John"
        storage.new(user)
        storage.save()
        storage.reload()
        self.assertEqual(len(storage.all()), 1)
        self.assertIsInstance(list(storage.all().values())[0], User)

    def test_adds_new_objects_to_dictionary(self):

        storage = FileStorage()
        user = User()
        user.name = "John"
        storage.new(user)
        storage.save()
        storage.reload()
        self.assertEqual(len(storage.all()), 1)

    def test_handles_missing_JSON_file(self):

        storage = FileStorage()
        storage.reload()
        self.assertEqual(len(storage.all()), 0)

    def test_handles_invalid_JSON_file(self):

        storage = FileStorage()
        with open(FileStorage.__file_path, 'w') as f:
            f.write("invalid json")
        storage.reload()
        self.assertEqual(len(storage.all()), 0)

    def test_handles_missing_or_incomplete_data(self):

        storage = FileStorage()
        with open(FileStorage.__file_path, 'w') as f:
            f.write('{"__class__": "User"}')
        storage.reload()
        self.assertEqual(len(storage.all()), 0)
