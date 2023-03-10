# -*- coding: utf-8 -*-
"""devops2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wnC-GgDYJOW46IEkYrB91CJHw_27JxDx
"""

import random
import json

# Define the structure of the work items
work_items = [
    {
        "fields": {
            "System.Title": "Work Item {}".format(i),
            "System.Description": "Description for Work Item {}".format(i),
            "System.AssignedTo": "User {}".format(random.randint(1, 10))
        }
    }
    for i in range(1000)
]

# Write the work items to a file
with open("work_items.json", "w") as f:
    f.write(json.dumps(work_items))