#! /usr/bin/env python3

import os
import requests
import locale

# Path to the data
path = "/supplier-data/descriptions/"
url = "http://[linux-instance-external-IP]/fruits"
keys = ["name", "weight", "description","image_name"]

# TODO: change below

folder = os.listdir(path)
for file in folder:
    keycount = 0
    fb = {}
    with open(path + file) as fl:
        for line in fl:
            if keycount == 1:
                # drop "lbs" and convert to an integer.
                value = line.strip()
                value = int(locale.atof(line.strip("lbs")))
            else:
                value = line.strip()
            fb[keys[keycount]] = value
            keycount += 1
    # add all fields, including the image_name
    value = os.path.basename(fl) + ".jpeg"
    fb[keys[keycount+=1]] = value

    print(file,fb)
    response = requests.post(url, json=fb)

print("body: ", response.request.body)
print("status: ",response.status_code)
