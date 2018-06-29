# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:30:28 2018

@author: Administrator
"""

from PIL import Image
import os

for filename in os.listdir(r"C:\Users\biglk\Downloads\Face Database"):
    if(filename[0] == 's'):
        test = Image.open(filename)
        test = test.resize((180,240),Image.BILINEAR)
        test.save(filename)
    