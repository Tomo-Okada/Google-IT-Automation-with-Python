#! /usr/bin/env python3

import os
import requests

# Path to the data
path = "/supplier-data/descriptions/"

# TODO: change below
keys = ["title", "name", "date", "feedback"]

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
    response = requests.post("http://35.223.242.101/feedback/",
    json=fb)
print("body: ", response.request.body)
print("status: ",response.status_code)
