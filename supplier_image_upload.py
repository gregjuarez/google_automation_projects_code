#!/usr/bin/env python3
import requests
import os,sys

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"


path = 'supplier-data/images/'

images = os.listdir(path)

for image in images:
    if image.endswith(".jpeg"):
        try:
            with open(path +image, 'rb') as opened:
                r = requests.post(url, files={'file': opened})
        except IOError:
            print("cannot upload", image)
