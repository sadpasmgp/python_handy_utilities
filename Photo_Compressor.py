'''
Photo Compressor with Anti-Aliasing in Python
'''

import os
from turtle import width
import PIL
from PIL import Image

location = r"E:\SnapsLifetime"
os.chdir(location)
filelist = os.listdir(location)

for file in filelist:
    #open the image
    with Image.open(file) as my_image:

        #new widht and height in px
        width = 3840
        height = 2160

        print("The original size of Image is: ", round(len(my_image.fp.read())/1024,2), "KB")

        #compressed the image
        my_image = my_image.resize((width,height),PIL.Image.NEAREST)
        my_image = my_image.resize((width // 2, height // 2), resample=Image.ANTIALIAS)

        #save the image
        my_image.save(f"E:\SnapsLifetime\compressed_images\{file}"+'compressedResized.jpg')

        #open the compressed image
        #with Image.open('compressedResized.jpg') as compresed_image:
            #print("The size of compressed image is: ", round(len(compresed_image.fp.read())/1024,2), "KB")