#! /usr/bin/env python3
import os
import requests
import json

#List all .txt files under /data/feedback directory
#that contains the actual feedback to be displayed
#on the company's website.
read_dir = "/data/feedback"
fd_list = os.listdir(read_dir)

#You should now have a list that contains all of the feedback files
#from the path /data/feedback. Traverse over each file and,
#from the contents of these text files, create a dictionary
#by keeping title, name, date, and feedback as keys for the content value, respectively.
path_list = []
url = "http://34.71.44.250/feedback"
keys = ["title", "name", "date", "feedback"]
# print("fd_list: ",fd_list)

for fd in fd_list:
    path_list.append(os.path.join(read_dir,fd))

# print("path_list: ",path_list)

for path in path_list:
    keycount = 0
    fb_dict = {}
    with open(path,"r") as file:
        for line in file:
            value = line.strip()
            fb_dict[keys[keycount]] = value
            keycount += 1
    print(path,fb_dict)
        # fb_dict["title"] = file.readline().strip()
        # fb_dict["name"] = file.readline().strip()
        # fb_dict["date"] = file.readline().strip()
        # fb_dict["feedback"] = file.readline().strip()
        # # fb_dicts.append(fb_dict)
    # json_data = json.dumps(fb_dict, indent=2)
    # print(json_data)
    response = requests.post(url, json=fb_dict)

#POST request to http://<corpweb-external-IP>/feedback.
#Replace <corpweb-external-IP> with corpweb's external IP address.
print(response.request.url)
print(response.request.body)

#Make sure an error message isn't returned.
response = requests.get(url)
print(response.raise_for_status())
