import json
from uuid import uuid4
from datetime import datetime
import os

class BaseModel:
    serialized_obj = {}

    # make it a class attribute so that its accessible everywhere
    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self) -> str:

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        to_json = self.__dict__
        to_json["__class__"] = self.__class__.__name__
        
        to_json["created_at"] = to_json["created_at"].isoformat()
        to_json["updated_at"] = to_json["updated_at"].isoformat()
        
        print(to_json)
        return to_json

    def new(self):
        key = f"{self.__class__.__name__}.{self.id}"
        return key

    def save(self) -> None:
        self.updated_at = datetime.now()

    #     print("searilsed_obj", self.serialized_obj)
    #     self.serialized_obj[self.new()] = self.to_dict()
    #     with open("file.json", "w") as file:
    #         json.dump(self.serialized_obj, file, indent=2)

    # def reload(self):
    #     with open("file.json", "r") as file:
    #         content = json.load(file)
    #         print(content)

    #         for k, v in content.items():
    #             # print("key", k)
    #             # print("value", v)

    #             self.serialized_obj[k] = v


# instantiate our class

model = BaseModel()
#model.to_dict()


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        
        self.__objects[key] = obj
        
    def save(self):
        serialized_obj = {}
        
        for k,v in self.__objects.items():
            serialized_obj[k] = v.to_dict()
            
            with open(self.__file_path, "w") as file:
                json.dump(serialized_obj, file, indent=2)
            
        
storage = FileStorage()
storage.new(model)
all_obj = storage.all()
#print(all_obj)
storage.save()
