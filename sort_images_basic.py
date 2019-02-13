import os
import shutil

org_dir = '/Users/sproul/Downloads/All_Image_and_Kernels'
blurry_dir = '/Users/sproul/Downloads/All_Image_and_Kernels/blurry'
not_blurry_dir = '/Users/sproul/Downloads/All_Image_and_Kernels/not_blurry'
kernal_dir = '/Users/sproul/Downloads/All_Image_and_Kernels/kernals'

def sort_imgs():
    for file in os.listdir(org_dir):

    # get all but the last 8 characters to remove
    # the index number and extension
    # print(str(file))

        file_name = str(file[:5])
        file_path = org_dir + '/' + str(file)

    # print(file_name)
    # print()
    # print(file_path)
    # print(f"First 5 characters of file_name: {file_name}")

        if file_name == 'image':
            # move files into created directory
            shutil.move(file_path, not_blurry_dir)

        if file_name == 'blurr':
            # move files into created directory
            shutil.move(file_path, blurry_dir)

        if file_name == 'kerne':
            # move files into created directory
            shutil.move(file_path, kernal_dir)




    # image, blurr, kerne,

    # dir_path = dir + dir_name
    # print(f'dir_path: {dir_path}')
    #
    # # check if directory exists or not yet
    # # if not os.path.exists(dir_path):
    # #     os.makedirs(dir_path)
    #
    # if os.path.exists(dir_path):
    #     file_path = dir + file
    #     print(f'file_path: {file_path}')
    #
    #     # move files into created directory
    #     shutil.move(file_path, dir_path)
