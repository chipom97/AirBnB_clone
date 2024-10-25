import json
from uuid import uuid4
from datetime import datetime
class Person:
    def __init__ (self) -> None:
        self.id = str(uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = self.created_at
    
    def __str__(self) -> str:
        
    	return f"id: {self.id} created_at: {self.created_at} updated_at: {self.updated_at}"
 
    def to_dict(self):
        to_json = self.__dict__
        to_json["__class__"] = self.__class__.__name__
        
        return to_json
    
    def new(self):
     key = f"{self.__class__.__name__}.{self.id}"
     return key
    
    
    
    def save(self):
        serialized_obj = {}
        serialized_obj [self.new()] = self.to_dict()
        with open('file.json', "a") as file:
            json.dump(serialized_obj, file, indent=2)

    
 
 
 
	
 
  
# instantiate our class

person1 = Person()
print(person1)
person1.save()
person_key = person1.new()
