# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 15:12:53 2021

@author: Alfy Benny
"""
import numpy as np

def out_xyz(path, atom_list, matrix):
    matrix = matrix.astype(np.str)
    final_mat = np.insert(matrix, 0, atom_list, axis=1)
    np.savetxt(path, final_mat, delimiter = " ", fmt = '%s')
    
def combine_files(file1, file2, file3):
    data = data2 = ""
    
    with open(file1) as fp:
        data = fp.read()
  
# Reading data from file2
    with open(file2) as fp:
        data2 = fp.read()
  
# Merging 2 files
# To add the data of file2
# from next line
    data += "\n"
    data += data2
  
    with open (file3, 'w') as fp:
        fp.write(data)