#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

import sys
import os

# Get the absolute path of the project's root directory
script_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(script_dir, '../../'))

# Add the project's root directory to sys.path
if project_root not in sys.path:
    sys.path.append(project_root)

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
