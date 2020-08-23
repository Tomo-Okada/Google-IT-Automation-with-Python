#! /usr/bin/env python3

import os
import requests
import locale
from collections import OrderedDict
import json

# Path to the data
path = "supplier-data/descriptions/"
url = "http://35.184.197.2/fruits"


folder = os.listdir(path)
for file in folder:
    keycount = 0
    # FIXME: dictionary does not retain order. It cause the error to upload JSON.
    fb = OrderedDict()
    name = file.split(".txt")[0]+".jpeg"

    with open(path + file) as fl:
        keys = ["name", "weight", "description","image_name"]
        fb["name"] = fl.readline().strip()
        fb["weight"] = int(fl.readline().strip(" lbs\n"))
        fb["description"] = fl.readline().strip()
        # add all fields, including the image_name
        fb["image_name"] = name

        # for line in fl:
        #     if keycount == 1:
        #         # drop "lbs" and convert to an integer.
        #         value = line.strip()
        #         value = line.strip(" lbs\n")
        #         value = int(value)
        #     else:
        #         value = line.strip()
        #
        #     fb[keys[keycount]] = value
        #     keycount += 1
    js = json.dumps(fb, indent=2, sort_keys=True)
    print(file,js)
    response = requests.post(url, json=js)

print("body: ", response.request.body)
print("status: ",response.status_code)
