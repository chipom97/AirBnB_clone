#!/usr/bin/python3

import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Navigate to the parent directory of the script’s directory
# Adjust the number of '..' as needed to reach the root directory
project_root = os.path.abspath(os.path.join(script_dir, '../../'))

print("Project root directory:", project_root)
