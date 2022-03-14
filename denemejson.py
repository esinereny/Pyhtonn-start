# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:51:48 2021

@author: user
"""

import json

with open("users.json") as users:
    data = json.load(users)
    print(data[0])