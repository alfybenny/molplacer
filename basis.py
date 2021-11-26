# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 14:21:51 2021

@author: Alfy Benny
"""
import numpy as np

# Get unit vector from the difference of two atom position coordinates
def get_unit_vec(indices, matrix):
    vec = matrix[indices[1]]-matrix[indices[0]]
    unit_vec = vec / np.linalg.norm(vec)
    return unit_vec

def get_unit_cross(vec1, vec2):
    vec = np.cross(vec1, vec2)
    unit_vec = vec / np.linalg.norm(vec)
    return unit_vec
# def get_basis(vec1, vec2):
#     return vec1 - vec2
