from file_storage import StorageEngine

"""
This code snippet represents a class called Console. The Console class is responsible for creating a console interface that allows users to interact with a storage engine. 

The Console class has the following methods:
- __init__(self, filename): Initializes the Console object by creating an instance of the StorageEngine class with the specified filename.
- run(self): Runs the console interface in a loop, prompting the user for commands and executing the corresponding methods based on the input.
- add_object(self): Prompts the user to enter an object ID and name, creates a dictionary object with the entered values, and adds it to the storage engine.
- update_object(self): Prompts the user to enter an object ID to update and a new object name, and updates the corresponding object in the storage engine with the new name.
- delete_object(self): Prompts the user to enter an object ID to delete, and deletes the corresponding object from the storage engine.
- list_objects(self): Retrieves all objects from the storage engine and prints their IDs and names.

To use this code snippet, create an instance of the Console class with a desired filename, and call the run() method to start the console interface.
"""
class Console:
    """
    Represents a console application that interacts with a StorageEngine to perform CRUD operations on objects.
    
    Example Usage:
    console = Console("data.txt")
    console.run()
    
    This code creates an instance of the Console class, passing the filename "data.txt" to the StorageEngine constructor. 
    It then calls the run method, which starts a loop to accept user commands and perform corresponding operations on objects.
    """
    
    def __init__(self, filename):
        """
        Initializes a Console instance with a StorageEngine instance using the provided filename.
        
        Args:
        - filename (str): The name of the file to be used by the StorageEngine.
        """
        self.storage_engine = StorageEngine(filename)

    def run(self):
        """
        Starts a loop to accept user commands and perform corresponding operations on objects.
        """
        while True:
            command = input("Enter a command: ")
            if command == "add":
                self.add_object()
            elif command == "update":
                self.update_object()
            elif command == "delete":
                self.delete_object()
            elif command == "list":
                self.list_objects()
            elif command == "quit":
                break
            else:
                print("Invalid command")

    def add_object(self):
        """
        Prompts the user to enter an object ID and name, creates an object dictionary, and adds it to the StorageEngine.
        """
        obj = {}
        obj_id = input("Enter object ID: ")
        if not obj_id:
            print("Invalid object ID")
            return
        obj['id'] = obj_id

        obj_name = input("Enter object name: ")
        if not obj_name:
            print("Invalid object name")
            return
        obj['name'] = obj_name

        self.storage_engine.add_object(obj)
        print("Object added successfully")

    def update_object(self):
        """
        Prompts the user to enter an object ID and a new object name, and updates the corresponding object in the StorageEngine.
        """
        try:
            obj_id = input("Enter object ID to update: ")
        except ValueError:
            print("Invalid object ID")
            return
        new_data = {}
        try:
            new_data['name'] = input("Enter new object name: ")
        except ValueError:
            print("Invalid object name")
            return
        self.storage_engine.update_object(obj_id, new_data)
        print("Object updated successfully")

    def delete_object(self):
        """
        Prompts the user to enter an object ID and deletes the corresponding object from the StorageEngine.
        """
        obj_id = input("Enter object ID to delete: ")
        if not obj_id:
            print("Invalid object ID")
            return

        self.storage_engine.delete_object(obj_id)
        print("Object deleted successfully")

    def list_objects(self):
        """
        Retrieves all objects from the StorageEngine and prints their IDs and names.
        """
        objects = self.storage_engine.load()
        for obj in objects:
            print(f"ID: {obj['id']}, Name: {obj['name']}")

filename = "data.json"  # Replace with your desired filename
console = Console(filename)
console.run()