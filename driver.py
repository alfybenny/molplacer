# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 17:52:01 2021

@author: Alfy Benny
"""

import input
import transform
import basis
import output
# import argparse

# parser = argparse.ArgumentParser(description = 'Arguments for defining the coefficients')
# parser.add_argument('file1', type = str, help = 'File containing eigenvectors for freq1')
# args = parser.parse_args()

x_choice = [11, 14]
y_choice = [14, 30]
scale = [1, 2, 3]


file = "test.xyz"

# Get 'matrix'
molecule_1 = input.xyz(file)
molecule_1.readfile()
coor_1 = molecule_1.get_np_array() 

# Get translate vector
unit_vec_x = basis.get_unit_vec(x_choice, coor_1)
unit_vec_y = basis.get_unit_vec(y_choice, coor_1)
unit_vec_z = basis.get_unit_cross(unit_vec_x, unit_vec_y)

translate_vec = scale[0]*(unit_vec_x) + scale[1]*(unit_vec_y) + scale[2]*(unit_vec_z)

coor_2 = transform.translate(coor_1, translate_vec)

molecule_1.readfile()
atom_list = molecule_1.get_atom_list()

# print(atom_list)
output.out_xyz('final.xyz', atom_list, coor_2)

