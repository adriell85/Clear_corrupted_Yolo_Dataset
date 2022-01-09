import glob
import numpy as np
import os

data = []
data_txt = []
data_png = []
path = 'dataset/'

# False = clear singles ".png" files
# True = clear singles ".txt" files
clear_txt_mode = False

if clear_txt_mode:
    for_parameter = data_txt
    conditional_search = data_png
    clear_extention = '.txt'
else:
    for_parameter = data_png
    conditional_search = data_txt
    clear_extention = '.png'


for image in glob.glob(path + '*'):
    file_with_extention = image.split('\\')[-1]
    path = image.split('\\')[0]
    file_name = file_with_extention.split('.')[0]

    if file_with_extention.split('.')[-1] == 'txt':
        data_txt.append(file_name)
    if file_with_extention.split('.')[-1] == 'png':
        data_png.append(file_name)


for text in for_parameter:
    if text in conditional_search:
        None
    else:
        os.remove(path + '\\' + text + clear_extention)