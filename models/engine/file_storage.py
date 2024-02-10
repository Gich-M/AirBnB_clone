import json
import os
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        if os.path.getsize(self.__file_path) > 0:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        else:
            self.__objects = {}