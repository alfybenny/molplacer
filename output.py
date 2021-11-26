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