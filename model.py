# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:30:28 2018

@author: Administrator
"""

from PIL import Image
import random
import os
import numpy as np


x_train = np.array([550,180,240,3],dtype = np.float)
y_train = np.array([100,180,240,3],dtype = np.float)

for filename in os.listdir(r"C:\Users\biglk\Downloads\Face Database"):
    if(filename[0] == 's'):
        test = Image.open(filename)
        
        num = int(filename[1]) * 10 + int(filename[2]) 
        matrix = np.array(test) / 255
        #print(matrix[0][0])
        
        
        
        
        
        
        
    
        
    