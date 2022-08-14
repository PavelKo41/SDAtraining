"""
A module can be deduced as a library
Each python file ".py" is treated as a module

import <<filename>>  # imports everything from a file
import <<filename>> as <<alias>> #renaiming a module
    import pandas as pd

from <<filename>> import <<Class,function>> #import specific items
    from collections import Counter
"""

from functions import my_name
my_name("Pavel", 29)


