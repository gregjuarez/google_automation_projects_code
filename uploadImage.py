#!/usr/bin/env python3
import os
from PIL import Image

path = 'supplier-data/images/'

for image in os.listdir(path):
    if "tiff" in image:
        file_name = os.path.splitext(image)[0]
        outfile = path + file_name + '.jpeg'
        try:
            img = Image.open(path + image).resize((600, 400)).convert("RGB").save(outfile,"JPEG")
        except IOError:
            print("cannot convert", image)
