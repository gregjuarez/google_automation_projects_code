#!/usr/bin/env python3
import os
from PIL import Image

old_path = os.path.expanduser('~') + '/images/'
new_path = '/opt/icons/'
for image in os.listdir(old_path):
    for image in os.listdir(old_path):
        if image == ".DS_Store":
            continue
        img = Image.open(old_path + image)
        img.rotate(-90).resize((128, 128)).convert("RGB").save(new_path + image + '.jpeg')
        img.close()

path = 'supplier-data/images/'

for image in os.listdir(path):
    if "tiff" in image:
        file_name = os.path.splitext(pic)[0]
        outfile = path + file_name + '.jpeg'
        try:
            img = Image.open(path + image).resize((600, 400)).convert("RGB").save(outfile,"JPEG")
            img.close()
        except IOError:
            print("cannot convert", image)

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)



from PIL import Image
import os, sys

path = "supplier-data/images/"
pictures = os.listdir(path)

for pic in pictures:
  if 'tiff' in pic:
    #grab the picture name without the .tiff extension
    file_name = os.path.splitext(pic)[0]
    outfile = "supplier-data/images/" + file_name + ".jpeg"
    try:
      Image.open(path + pic).convert("RGB").resize((600,400)).save(outfile,"JPEG")
    except IOError:
      print("cannot convert", pic)
