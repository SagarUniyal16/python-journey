# python_import_examples.py
# Demonstrate various import styles and best practices in Python

##############################
# 2. Basic Import
import math
print("math.sqrt(16):", math.sqrt(16))  # 4.0

##############################
# 3. Import Specific Functions
from math import sqrt, pi
print("sqrt(25):", sqrt(25), "; pi:", pi)  # 5.0 3.14159...

##############################
# 4. Import with Alias
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(6).reshape(2, 3))
print("Pandas DataFrame:\n", df)

##############################
# 5. Import All (Avoid in practice)
# from math import *
# print(sin(pi/2))  # Not recommended

##############################
# 6. Custom Module Import
# Save this part in a separate file called my_utils.py in the same directory:
# def greet(name):
#     return f"Hello, {name}!"

import my_utils  # Make sure my_utils.py is present
print("Greeting from custom module:", my_utils.greet("Sagar"))

##############################
# 7. Import from Packages
# Folder structure:
# project/
#   └── data/
#         ├── __init__.py
#         └── cleaner.py
# cleaner.py should have:
# def clean_data(data):
#     return [x.strip() for x in data]

# from data.cleaner import clean_data
# print(clean_data(["  abc ", " xyz "]))  # Uncomment if structure exists

##############################
# 8. Relative Imports (inside packages only)
# Only works if inside a package
# from . import helper           # same package
# from ..utils import logger     # parent package

##############################
# 9. Reload Module
import importlib
importlib.reload(my_utils)  # Re-executes the code in my_utils.py

##############################
# 10. Find Module Path
print("math module path:", math.__file__)

##############################
# 11. Common Built-in Modules
import sys
import os
import datetime
import random
print("Random number:", random.randint(1, 10))
print("Current directory:", os.getcwd())
print("Python version:", sys.version)
print("Today's date:", datetime.date.today())

##############################
# 12. Best Practices
# - Import only what is needed
# - Keep imports at the top
# - Use alias naming for readability
# - Avoid 'from module import *'
# - Order: standard library, third-party, local

import os
import sys

import pandas as pd
import numpy as np

from my_utils import greet   # Example of specific function import

print("Ordered imports and single function import:", greet("World"))


# End of file
