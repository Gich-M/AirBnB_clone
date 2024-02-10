"""
This code snippet initializes a FileStorage object and reloads its contents. The FileStorage class is imported from the engine.file_storage module. The reload() method is called on the storage object to reload its contents. This code is typically used to initialize and load data into a FileStorage object.
"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
