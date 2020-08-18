#! /usr/bin/env python3
import os
import requests
import json

#List all .txt files under /data/feedback directory
#that contains the actual feedback to be displayed
#on the company's website.
path_list = os.listdir("/data/feedback")

#You should now have a list that contains all of the feedback files
#from the path /data/feedback. Traverse over each file and,
#from the contents of these text files, create a dictionary
#by keeping title, name, date, and feedback as keys for the content value, respectively.
fb_dict = {}

for path in path_list:
    with open(path,"r") as file:
        fb_dict["title"] = file.readline().split()
        fb_dict["name"] = file.readline().split()
        fb_dict["date"] = file.readline().split()
        fb_dict["feedback"] = file.readline().split()
        #test#
        print(fb_dict)

#POST request to http://<corpweb-external-IP>/feedback.
#Replace <corpweb-external-IP> with corpweb's external IP address.
url = "http://<corpweb-external-IP>/feedback"
response = requests.post(url, data=fb_dict)

#Make sure an error message isn't returned.
response = requests.get(url)
response.raise_for_status()
