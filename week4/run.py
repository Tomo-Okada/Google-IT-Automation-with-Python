#! /usr/bin/env python3

import os
import requests

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
            value = line.strip()
            fb[keys[keycount]] = value
            keycount += 1
    print(file,fb)
    response = requests.post(url,
    json=fb)
print("body: ", response.request.body)
print("status: ",response.status_code)
