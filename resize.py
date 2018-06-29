# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:30:28 2018

@author: Administrator
"""

from PIL import Image
import os

path = r"./Face Database"

for filename in os.listdir(path):
    if(filename[0] == 's'):
        test = Image.open(path+'\\'+filename)
        test = test.resize((180,240),Image.BILINEAR)
        test.save(filename)
    