import os
import json
from datetime import datetime
import uuid

"""
This code snippet defines a class called StorageEngine. The class provides methods for saving, loading, adding, updating, and deleting objects in a file using JSON format. 

The class has the following methods:
- __init__(self, filename): Initializes the StorageEngine object with a filename. If the file does not exist, it creates an empty file.
- save(self, objects): Saves the given objects to the file in JSON format.
- load(self): Loads the objects from the file and returns them as a list.
- add_object(self, obj): Adds a new object to the file. The object must be a dictionary and it will be assigned a unique ID and timestamp.
- update_object(self, obj_id, new_data): Updates an existing object in the file with new data. The object is identified by its ID.
- delete_object(self, obj_id): Deletes an object from the file. The object is identified by its ID.

Note: The code snippet assumes that the file exists and is accessible for read and write operations.
"""
class StorageEngine:
    def __init__(self, filename):
        """
        Initializes a new instance of the StorageEngine class.

        Args:
            filename (str): The name of the file to be used for storing data.

        Raises:
            ValueError: If the filename is empty.
            Exception: If there is an error creating the file.

        """
        if filename == "":
            raise ValueError("Filename cannot be empty")
        self.filename = filename
        try:
            if not os.path.exists(self.filename):
                open(self.filename, 'a').close()
        except OSError as e:
            raise Exception(f"Error creating file: {e}")


    def save(self, objects):
        """
        Save a list of objects to a file in JSON format with an indentation of 4 spaces.

        Args:
            objects (list): A list of objects to be saved to the file.

        Raises:
            Exception: If there is an OSError while opening the file.
            Exception: If there is a json.JSONDecodeError while encoding the objects as JSON.

        Returns:
            None. The method saves the objects to the file specified by self.filename.
        """
        try:
            with open(self.filename, 'w') as f:
                json.dump(objects, f, indent=4)
        except OSError as e:
            raise Exception(f"Error saving objects: {e}")
        except json.JSONDecodeError as e:
            raise Exception(f"Error encoding objects as JSON: {e}")

    def load(self):
        """
        Load data from a file in JSON format.

        Returns:
            list: A list of objects loaded from the file. If the file does not exist, an empty list is returned.

        Raises:
            ValueError: If the loaded data is not a list, indicating that the data file is corrupted.
            Exception: If there is an error loading or decoding the objects from JSON.

        Example Usage:
            storage = StorageEngine("data.json")
            data = storage.load()
            print(data)
        """
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                if not isinstance(data, list):
                    raise ValueError("Corrupted data file: data should be a list")
                return data
        except FileNotFoundError:
            return []
        except OSError as e:
            raise Exception(f"Error loading objects: {e}")
        except json.JSONDecodeError as e:
            raise Exception(f"Error decoding objects from JSON: {e}")
            return []

    def add_object(self, obj):
        """
        Adds a new object to the list of objects and saves it to a file.

        Args:
            obj (dict): The object to be added to the list.

        Raises:
            ValueError: If the obj parameter is not a dictionary.
            Exception: If there is an error generating the UUID or timestamp.

        Example Usage:
            storage = StorageEngine("data.json")  # Initialize the StorageEngine object with the filename
            obj = {"name": "John", "age": 30}  # Create a dictionary object to be added
            storage.add_object(obj)  # Add the object to the list and save it to the file
        """
        if not isinstance(obj, dict):
            raise ValueError("obj must be a dictionary")
        try:
            obj['id'] = str(uuid.uuid4())
        except Exception as e:
            raise Exception(f"Error generating UUID: {e}")
        try:
            obj['created_at'] = datetime.now().isoformat()
            obj['updated_at'] = datetime.now().isoformat()
        except Exception as e:
            raise Exception(f"Error generating timestamp: {e}")
        objects = self.load()
        objects.append(obj)
        self.save(objects)


    def update_object(self, obj_id, new_data):
        """
        Update an object in the list of objects stored in a file.

        Args:
            obj_id (str): The ID of the object to be updated.
            new_data (dict): The new data for the object.

        Raises:
            ValueError: If obj_id is None.

        Example Usage:
            storage = StorageEngine("data.json")  # Initialize the StorageEngine object with the filename
            obj_id = "12345"  # ID of the object to be updated
            new_data = {"name": "John Doe", "age": 35}  # New data for the object
            storage.update_object(obj_id, new_data)  # Update the object with the new data
        """
        if obj_id is None:
            raise ValueError("obj_id cannot be None")
        objects = self.load()
        for obj in objects:
            if obj.get('id') == obj_id:
                obj.update(new_data)
                obj['updated_at'] = datetime.now().isoformat()
                self.save(objects)
                return

    def delete_object(self, obj_id):
        """
        Deletes an object from the list of objects stored in a file by marking it as deleted.

        Args:
            obj_id (str): The ID of the object to be deleted.

        Raises:
            ValueError: If obj_id is None.

        Example Usage:
            storage = StorageEngine("data.json")  # Initialize the StorageEngine object with the filename
            obj_id = "12345"  # ID of the object to be deleted
            storage.delete_object(obj_id)  # Delete the object with the specified ID

        """
        if obj_id is None:
            raise ValueError("obj_id cannot be None")
        objects = self.load()
        for obj in objects:
            if obj.get('id') == obj_id:
                obj['deleted_at'] = datetime.now().isoformat()
        objects = [obj for obj in objects if obj.get('deleted_at') is None]
        self.save(objects)

