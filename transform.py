# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:55:18 2021

@author: Alfy Benny
"""
import numpy as np

def translate(A, vec):
    B = A.__add__(vec)
    return B

def rotate(axis, A, theta):
    if axis == 'x':
        R = np.array(((1, 0, 0), (0, np.cos(theta), -np.sin(theta)), (0, np.sin(theta), np.cos(theta))))
        
    elif axis == 'y':
        R = np.array(((np.cos(theta), 0, np.sin(theta)), (0, 1, 0), (-np.sin(theta), 0, np.cos(theta))))
    
    elif axis == 'z':
        R = np.array(((np.cos(theta), -np.sin(theta), 0), (np.sin(theta), np.cos(theta), 0), (0, 0, 1)))
    
    B = A.dot(R)
    return B

def molecule_rotate(A, rotate_vec):
    B = rotate('x', A, rotate_vec[0])
    C = rotate('y', B, rotate_vec[1])
    D = rotate('z', C, rotate_vec[2])
    
    return D


