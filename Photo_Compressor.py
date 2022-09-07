'''
Photo Compressor with Anti-Aliasing in Python
'''

import os
from turtle import width
import PIL
from PIL import Image

location = r"E:\Snaps Lifetime\202006 Simran Sadiq Nikah"
os.chdir(location)
filelist = os.listdir(location)

for file in filelist:
    #open the image
    with Image.open(file) as my_image:

        # get width and height
        width,height = my_image.size
  
        # display width and height
        print("The height of the image is: ", height)
        print("The width of the image is: ", width)

        print("The original size of Image is: ", round(len(my_image.fp.read())/1024,2), "KB")

        #compressed the image
        width = width//2
        height = height//2
        
        my_image = my_image.resize((width,height),PIL.Image.NEAREST)
        my_image = my_image.resize((width // 2, height // 2), resample=Image.ANTIALIAS)

        #save the image
        my_image.save(f"E:\Snaps Lifetime\compressed_images\{file}")

        #open the compressed image
        with Image.open(file) as compresed_image:
            print("The size of compressed image is: ", round(len(compresed_image.fp.read())/1024,2), "KB")
            print('\n')
