import json
from uuid import uuid4
from datetime import datetime
import os

class Person:
    serialized_obj = {}

    # make it a class attribute so that its accessible everywhere
    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = self.created_at

    def __str__(self) -> str:

        return (
            f"id: {self.id} created_at: {self.created_at} updated_at: {self.updated_at}"
        )

    def to_dict(self):
        to_json = self.__dict__
        to_json["__class__"] = self.__class__.__name__

        return to_json

    def new(self):
        key = f"{self.__class__.__name__}.{self.id}"
        return key

    def save(self):

        print("searilsed_obj", self.serialized_obj)
        self.serialized_obj[self.new()] = self.to_dict()
        with open("file.json", "w") as file:
            json.dump(self.serialized_obj, file, indent=2)

    def reload(self):
        with open("file.json", "r") as file:
            content = json.load(file)
            print(content)

            for k, v in content.items():
                # print("key", k)
                # print("value", v)

                self.serialized_obj[k] = v


# instantiate our class

person1 = Person()
import json
from uuid import uuid4
from datetime import datetime


class Person:
    serialized_obj = {}

    # make it a class attribute so that its accessible everywhere
    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = self.created_at

    def __str__(self) -> str:

        return (
            f"id: {self.id} created_at: {self.created_at} updated_at: {self.updated_at}"
        )

    def to_dict(self):
        to_json = self.__dict__
        to_json["__class__"] = self.__class__.__name__

        return to_json

    def new(self):
        key = f"{self.__class__.__name__}.{self.id}"
        return key

    def save(self):

        print("searilsed_obj", self.serialized_obj)
        self.serialized_obj[self.new()] = self.to_dict()
        with open("file.json", "w") as file:
            json.dump(self.serialized_obj, file, indent=2)

    def reload(self):
        with open("file.json", "r") as file:
            try:
                if os.path.getsize("file.json") > 0:
                    content = json.load(file)

                    for k, v in content.items():
                        # print("key", k)
                        # print("value", v)
                        self.serialized_obj[k] = v
            except json.decoder.JSONDecodeError:
                print("Unable to decode file storage")


# instantiate our class

person1 = Person()
person1.reload()
person1.save()
