# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:55:18 2021

@author: Alfy Benny
"""

import input

file = "test.xyz"

file1 = input.xyz(file)
file1.readfile()
M = file1.extract_coordinate()

print(M)
