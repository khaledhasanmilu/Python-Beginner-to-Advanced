# Built-in modules
import os
import sys
import math
import random
import datetime
import time
import json
import re
import statistics

# Third-party modules (install with pip if needed)
# import numpy as np
# import requests
# import pandas as pd

# 1. os – Operating system interaction
print("Current working directory:", os.getcwd())

# 2. sys – System-specific functions
print("Python version:", sys.version)

# 3. math – Mathematical functions
print("Square root of 16:", math.sqrt(16))

# 4. random – Random numbers
print("Random number between 1 and 100:", random.randint(1, 100))

# 5. datetime – Date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# 6. time – Time-related functions
print("Sleeping for 1 second...")
time.sleep(1)
print("Awake!")

# 7. json – JSON handling
person = {"name": "Alice", "age": 30}
person_json = json.dumps(person)
print("JSON string:", person_json)

# 8. re – Regular expressions
text = "The rain in Spain"
match = re.search(r"Spain", text)
print("Regex match found:", bool(match))

# 9. statistics – Basic statistics
data = [10, 20, 30, 40, 50]
print("Mean of data:", statistics.mean(data))

# Uncomment below if you have third-party modules installed:
# 10. numpy – Numerical computing
# array = np.array([1, 2, 3])
# print("NumPy array:", array)

# 11. requests – HTTP requests
# response = requests.get("https://api.github.com")
# print("GitHub API status code:", response.status_code)

# 12. pandas – Data analysis
# df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
# print("Pandas DataFrame:\n", df)
