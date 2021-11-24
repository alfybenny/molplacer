# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:55:18 2021

@author: Alfy Benny
"""

import numpy as np
from abc import ABC, abstractmethod

file = "test.xyz"

class input_processing:
    
    
    content = []
    matrix = []
    
    # The filetype could be .xyz, .mol2, .cif etc.
    def __init__(self, file):
       self.file = file

    def readfile(self):
        # Reading file contents
        self.content = open(file, 'r')
        return self.content
        
   
    # Abstract class for getting coordiantes from the read file
    @abstractmethod
    def extract_coordinate(self):
        pass

# SUBCLASS-INPUT_PROCESSING==========================================
# Get coordinates from file for .xyz fileformat
# NOTE: class xyz knows what is content
class xyz(input_processing):
    def extract_coordinate(self):
        # SOURCE: https://stackoverflow.com/questions/7618858/how-to-to-read-a-matrix-from-a-given-file
        with self.content as f:
            self.matrix = [[str(num) for num in line.split('\n')] for line in f if line.strip() != " "]
            return self.matrix
        return self.matrix

# Get coordinates from file for .mol2 fileformat
class mol2(input_processing):
    def readfile(self):
        print("mol2")

# Get coordinates from file for .cif fileformat
class cif(input_processing):
    def readfile(self):
        print("cif")
        

