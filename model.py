# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:30:28 2018

@author: Administrator
"""

from PIL import Image
import random
import os
import numpy as np


x_train = []
x_one_hot = []

y_test = []
y_one_hot = []



for filename in os.listdir(r"C:\Users\biglk\Downloads\Face Database"):
    if(filename[0] == 's'):
        test = Image.open(filename)
        
        num = int(filename[1]) * 10 + int(filename[2]) 
        matrix = np.array(test) / 255
        num_temp = int(filename[4]) * 10 + int(filename[5]) 
        #print(matrix[0][0])
        
        if(num_temp >= 14):
            y_test.append(matrix)
            y_one_hot.append(num)
           
        else:
            x_train.append(matrix)
            x_one_hot.append(num)
            
x_data = np.array(x_train)
x_label = np.array(x_one_hot)          

y_data = np.array(y_test)
y_label = np.array(y_one_hot)

print(x_data.shape)
print(y_data.shape)
        
        
        
        
        
    
        
    