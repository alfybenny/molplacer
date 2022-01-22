# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 17:52:01 2021

@author: Alfy Benny
"""

import input
import transform
import basis
import output
import argparse

parser = argparse.ArgumentParser(description = 'Arguments for defining the coefficients')
parser.add_argument('file', type = str, help = 'File containing eigenvectors for freq1')
# parser.add_argument('file1', type = str, help = 'File containing eigenvectors for freq1')
parser.add_argument('x_choice1', type = int, help = 'atom indices for defining x axis')
parser.add_argument('x_choice2', type = int, help = 'atom indices for defining x axis')
parser.add_argument('y_choice1', type = int, help = 'atom indices for defining y axis')
parser.add_argument('y_choice2', type = int, help = 'atom indices for defining y axis')
parser.add_argument('scale_x', type = float, help = 'enter the translate length in x axis (angstrom)')
parser.add_argument('scale_y', type = float, help = 'enter the translate length in y axis (angstrom)')
parser.add_argument('scale_z', type = float, help = 'enter the translate length in z axis (angstrom)')
parser.add_argument('rotate_x', type = float, help = 'enter the angle theta in x axis (radians)')
parser.add_argument('rotate_y', type = float, help = 'enter the angle theta in y axis (radians)')
parser.add_argument('rotate_z', type = float, help = 'enter the angle theta in z axis (radians)')
args = parser.parse_args()

# Processing input
x_choice = [args.x_choice1, args.x_choice2]
y_choice = [args.y_choice1, args.y_choice2]
scale = [args.scale_x, args.scale_y, args.scale_z]
rotate = [args.rotate_x, args.rotate_y, args.rotate_z]

file = args.file

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
coor_3 = transform.molecule_rotate(coor_2, rotate)

output.plot_molecule(coor_1, coor_3)

molecule_1.readfile()
atom_list = molecule_1.get_atom_list()

# print(atom_list)
file_name = 'final.xyz'
output.out_xyz(file_name, atom_list, coor_3)


output.combine_files(file, file_name, 'combined.xyz')


