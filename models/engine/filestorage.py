print("before import of the file storage")

print("Last part of file storage")
import json


# filestorage.py
class FileStorage:

    # map every clas that  we create in this dictionary
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"

        self.__objects[key] = obj

    def save(self):
        serialized_obj = {}

        for k, v in self.__objects.items():
            serialized_obj[k] = v.to_dict()

            with open(self.__file_path, "w") as file:
                json.dump(serialized_obj, file, indent=2)

    def reload(self):
        from models.basemodel import BaseModel

        CLASSES = {"BaseModel": BaseModel}
        with open(self.__file_path, "r") as file:
            content = json.load(file)

            for k, v in content.items():

                class_name = v["__class__"]

                if class_name in self.CLASSES:
                    instance = self.CLASSES[class_name](**v)

                    print("reloaded_instance", instance)

                    self.__objects[k] = instance


print("Last part of file storage")
