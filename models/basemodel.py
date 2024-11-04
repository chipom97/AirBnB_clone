# basemodel.py
print("basemodel imported")
from uuid import uuid4
from datetime import datetime

# import os
from models.engine.filestorage import FileStorage


class BaseModel:

    # make it a class attribute so that its accessible everywhere
    def __init__(self, **kwarg) -> None:

        if kwarg:
            for k, v in kwarg.items():
                if k == "__class__":
                    continue

                if k in ["created_at", "updated_at"] and isinstance(k, str):
                    v = datetime.fromisoformat(v)

                setattr(self, k, v)

        else:

            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self) -> str:

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        self.updated_at = datetime.now()

    def to_dict(self):
        to_json = self.__dict__
        to_json["__class__"] = self.__class__.__name__

        to_json["created_at"] = to_json["created_at"].isoformat()
        to_json["updated_at"] = to_json["updated_at"].isoformat()
        print(to_json)
        return to_json


model = BaseModel()
storage = FileStorage()
print(model)
