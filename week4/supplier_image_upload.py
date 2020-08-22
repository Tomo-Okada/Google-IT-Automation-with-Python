#!/usr/bin/env python3
import requests

read_dir = "/supplier-data/images"
url = "http://localhost/upload/"

for file_name in glob.glob(os.path.join(read_dir,"*.jpeg")):
    with open(file_name, 'rb') as opened:
    r = requests.post(url, files={'file': opened})
