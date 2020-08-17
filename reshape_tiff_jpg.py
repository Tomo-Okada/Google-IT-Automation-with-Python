#!/usr/bin/env python3
from PIL import Image
import glob, os

read_dir = "images"
save_dir = "opt/icons"

for file_name in glob.glob(os.path.join(read_dir,"*")):
    im = Image.open(file_name)
    new_im = im.rotate(90, expand=True).resize((128,128)).convert('RGB')
    basename = os.path.basename(file_name)
    print(basename)
    new_im.save(os.path.join(save_dir,basename),format='jpeg')

    # new_im.save(os.path.join(save_dir,basename),format='jpeg')
    # new_im.save(os.path.join(save_dir,basename),format='jpeg')
