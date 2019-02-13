import os
import shutil

# Function to rename multiple files

path = '/Users/sproul/Downloads/mod5_blinkORnot_pics/'

def rename_files(path):

    i = 1

    for f in os.listdir(path):
        dst = 'open' + str(i) + '.jpg'
        src = xxxx + f
        dst = xxxx + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)
        i += 1
