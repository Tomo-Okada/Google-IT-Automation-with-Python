#! /usr/bin/env python3

import os
import requests
import locale
from collections import OrderedDict
import json

# Path to the data
path = "supplier-data/descriptions/"
url = "http://localhost/fruits/"


folder = os.listdir(path)
for file in folder:
    fb = {} #OrderedDict()
    with open(path + file,"r") as fl:
        fb.clear()
        keys = ["name", "weight", "description","image_name"]
        fb["name"] = fl.readline().strip("\n")
        fb["weight"] = int(fl.readline().strip("\n").strip("lbs"))
        fb["description"] = fl.readline().strip("\n")
        fb["image_name"] = file.split(".txt")[0]+".jpeg"

    # js = json.dumps(fb, indent=2)
    # NOTE: JSON dump makes post unworkable. Instead, dictionaries format works well in below.
    response = requests.post(url, json=fb)
    print(file,fb)

print(response.raise_for_status())
print("body: ", response.request.body)
print("status: ",response.status_code)
