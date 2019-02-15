import os
import sys
import shutil
from os import system
from pathlib import Path

import cv2
import dlib
import keras
import imutils
import argparse
import numpy as np
import pandas as pd
from imutils import face_utils
from keras.models import Sequential, Model
from keras.preprocessing.image import array_to_img, img_to_array, load_img
import matplotlib.pyplot as plt
# from keras.optimizers import Adam, RMSprop
# from keras.activations import relu
# from keras.applications import VGG16, VGG19
# from keras.preprocessing.image import ImageDataGenerator
# from keras.layers import Conv2D, Flatten, Dense, Activation, Dropout, InputLayer
# from keras.layers import ZeroPadding2D, Convolution2D, MaxPooling2D
# from keras.layers import GlobalAveragePooling2D, LeakyReLU
# from keras.applications import MobileNet
# from keras.preprocessing import image
# from keras.applications.mobilenet import preprocess_input
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import PCA
# from sklearn.metrics import f1_score, accuracy_score


os.environ['KMP_DUPLICATE_LIB_OK']='True'
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


# os.mkdir(str(Path.home()) + '/Desktop/testing_this_shizzzz')

# Paths to be created

home_path = str(Path.home()) + '/Desktop'
blurry_dir = home_path + "/these_should_be_blurry"
not_blurry_dir = home_path + "/no_blurry_images_here"


# Create paths for sorting blurry images from non-blurry
def create_folders():

    if os.path.isdir(blurry_dir):
        pass
    else:
        os.mkdir(blurry_dir)
        print()
        print('Blurry directory created')
        print()
    if os.path.isdir(not_blurry_dir):
        pass
    else:
        os.mkdir(not_blurry_dir)
        print('Not blurry directory created')
        print()

    # print()
    # print()
    # print('Paths were created')
    # print()
    # print()
    # print('Please, set the path of the folder you wish to sort')
    # print('The path variable should be defined as a string named "dir_path"')


model_path = str(Path.home()) + '/Desktop/ds-projects/mod5_project/testing_model_save'

cnn = keras.models.load_model(model_path)

# function to predict image classes
def predict_image_cnn(path):
    img = load_img(path, target_size=(224, 224))
    plt.imshow(img)
    img = img_to_array(img)

    img = img/255
    img = np.expand_dims(img, axis=0)
    predict = cnn.predict(img)
    return predict


# Define folder we want to sort
# dir_path = 'THIS IS THE FOLDER WE WANT TO SORT WITH FUNCTION BELOW'
# reset_default_path = ''

default_dir_path = '/Users/sproul/Downloads/mod5_imgs/slide_imgs/'



# Define funtion to sort blurry from not blurry
def sort_blurry(dir_path):

    create_folders()

    for file in os.listdir(dir_path):

        file_path = dir_path + str(file)
        file_name = str(file[:-3])
        file_ext = str(file[-3:])

        if file_ext == 'jpg':
            blurry_pred = predict_image_cnn(file_path)
            print(file_name, blurry_pred)


        if blurry_pred > 0.5:
            shutil.move(file_path, blurry_dir)

        else:
            shutil.move(file_path, not_blurry_dir)
    print()
    print('🤓 📷 🤓 📷 🤓 📷 🤓 📷 🤓 📷 🤓 📷 🤓 📷 🤓 📷 🤓 📷 🤓 📷 🤓')
    print('The potentially "blurry" photographs have been sorted!')
    print('🤓 📷 🤓 📷 🤓 📷 🤓 📷 🤓 📷 🤓 📷 🤓 📷 🤓 📷 🤓 📷 🤓 📷 🤓')
    print()

    system('say -v Oliver Your photographs have been processed')




# THIS FUNCTION IS NOT READY. NEEDS TO BE INTEGRATED ASAP.

# Define a function to sort blinks from not blinks

# def sort_blinks(dir_path):
#
#     for file in os.listdir(dir_path):
#
#         file_path = dir_path + '/' + str(file)
#
#         leftEye, rightEye = cropEyes(file)
#         leftEye_pred = model.predict(leftEye)
#         rightEye_pred = model.predict(rightEye)
#
#         if leftEye_pred < .5 or rightEye_pred < .5:
#             shutil.move(file_path, blink_dir)
#         else:
#             shutil.move(file_path, not_blink_dir)




# The following function is to reset the folders during project presentation

def reset_presentation():

    for file in os.listdir(blurry_dir):
        file_path = blurry_dir +  '/' + str(file)
        file_ext = str(file[-3:])
        if file_ext == 'jpg':
            shutil.move(file_path, default_dir_path)

    for file in os.listdir(not_blurry_dir):
        file_path = not_blurry_dir +  '/' + str(file)
        file_ext = str(file[-3:])
        if file_ext == 'jpg':
            shutil.move(file_path, default_dir_path)



if __name__ == '__main__':

    sort_blurry(default_dir_path)
