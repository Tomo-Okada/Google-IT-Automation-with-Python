#!/usr/bin/env python3
from PIL import Image
import glob, os

read_dir = "supplier-data/images"
save_dir = "supplier-data/images"

for file_name in glob.glob(os.path.join(read_dir,"*.tiff")):
    im = Image.open(file_name)
    #Size: Change image resolution from 3000x2000 to 600x400 pixel
    #Format: Change image format from .TIFF to .JPEG
    #Use convert("RGB") method for converting RGBA to RGB image.
    new_im = im.resize((600,400)).convert('RGB')
    basename = os.path.basename(file_name)
    basename = basename.split(".tiff")[0]+".jpeg"
    print(basename)
    #Save them in the same path ~/supplier-data/images, with a JPEG extension.
    new_im.save(os.path.join(save_dir,basename),format='jpeg')
